#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <map>
#include <ctime>
#include <iomanip>
using namespace std;

struct BookInfo {
    int totalQuantity = 0;
    int availableQuantity = 0;
};

struct BookIssueRecord {
    string bookName;
    time_t issueTime;
    time_t dueTime;
};

struct Student {
    string name;
    int id_no;
    string stream;
    vector<BookIssueRecord> issuedBooks;
};

class BST {
    struct Node {
        string key;
        Node* left;
        Node* right;
        Node(string val) : key(val), left(nullptr), right(nullptr) {}
    };
    Node* root;

    Node* insertRec(Node* node, const string& key) {
        if (!node) return new Node(key);
        if (key < node->key)
            node->left = insertRec(node->left, key);
        else if (key > node->key)
            node->right = insertRec(node->right, key);
        return node;
    }

    bool search(Node* node, const string& key) {
        if (!node) return false;
        if (key == node->key) return true;
        return key < node->key ? search(node->left, key) : search(node->right, key);
    }

    void inorder(Node* node) {
        if (!node) return;
        inorder(node->left);
        cout << node->key << " ";
        inorder(node->right);
    }

public:
    BST() : root(nullptr) {}
    void insert(const string& key) { root = insertRec(root, key); }
    bool contains(const string& key) { return search(root, key); }
    void printInOrder() { inorder(root); cout << endl; }
};
void saveBooks(const unordered_map<string, BookInfo>& books) {
    ofstream fout("books.txt");
    for (const auto& [name, info] : books) {
        fout << name << "," << info.totalQuantity << "," << info.availableQuantity << "\n";
    }
}
void loadBooks(unordered_map<string, BookInfo>& books, BST& bookTree) {
    ifstream fin("books.txt");
    string line;
    while (getline(fin, line)) {
        stringstream ss(line);
        string name;
        int total, available;

        getline(ss, name, ',');
        ss >> total;
        ss.ignore(); // skip comma
        ss >> available;

        books[name] = {total, available};
        bookTree.insert(name); // ✅ Rebuild the BST
    }
}
void saveStudents(const map<int, Student>& students) {
    ofstream fout("students.txt");
    for (const auto& [id, stu] : students) {
        fout << id << "," << stu.name << "," << stu.stream << "\n";
    }
}
void loadStudents(map<int, Student>& students) {
    ifstream fin("students.txt");
    string line;
    while (getline(fin, line)) {
        stringstream ss(line);
        string id_str, name, stream;
        getline(ss, id_str, ',');
        getline(ss, name, ',');
        getline(ss, stream);

        int id = stoi(id_str);
        students[id] = {name, id, stream};
    }
}


void printTime(const string& label, time_t t) {
    tm* tm_info = localtime(&t);
    cout << label << put_time(tm_info, "%d/%m/%Y %H:%M:%S") << endl;
}

int main() {
    unordered_map<string, BookInfo> books;
    map<int, Student> students;
    BST bookTree;

loadBooks(books, bookTree);
loadStudents(students);

    int choice;
    while (true) {
        cout << "\n1. Librarian Login\n2. Student Login\n3. Exit\nEnter choice: ";
        cin >> choice;

        if (choice == 1) {
            string uid, pwd;
            cout << "Enter UserID: ";
            cin >> uid;
            cout << "Enter Password: ";
            cin >> pwd;
            if (uid != "admin" || pwd != "1234") {
                cout << "Invalid login!\n";
                continue;
            }
            int libChoice;
            while (true) {
                cout << "\n1. Add Book\n2. Update Quantity\n3. View Books\n4. View Inorder\n5. Back\nEnter choice: ";
                cin >> libChoice;
                if (libChoice == 5) break;
                if (libChoice == 1) {
                    string book;
                    int qty;
                    cout << "Enter book name: ";
                    cin >> book;
                    cout << "Enter quantity: ";
                    cin >> qty;
                    if (!bookTree.contains(book))
                        bookTree.insert(book);
                    books[book].totalQuantity += qty;
                    books[book].availableQuantity += qty;
                    cout << "Book added.\n";
                } else if (libChoice == 2) {
                    string book;
                    int qty;
                    cout << "Enter book name: ";
                    cin >> book;
                    if (!books.count(book)) {
                        cout << "Book not found.\n";
                        continue;
                    }
                    cout << "Enter additional quantity: ";
                    cin >> qty;
                    books[book].totalQuantity += qty;
                    books[book].availableQuantity += qty;
                    cout << "Book quantity updated.\n";
                } else if (libChoice == 3) {
                    for (auto& b : books) {
                        cout << b.first << ": Total=" << b.second.totalQuantity
                             << ", Available=" << b.second.availableQuantity << endl;
                    }
                } else if (libChoice == 4) {
                    bookTree.printInOrder();
                }
            }

        } else if (choice == 2) {
int stuMainChoice;
cout << "\n1. Create New Student Account\n2. Login as Existing Student\nEnter choice: ";
cin >> stuMainChoice;

int sid;
if (stuMainChoice == 1) {
    string name, stream;
    cout << "Enter new Student ID: ";
    cin >> sid;
    if (students.count(sid)) {
        cout << "Student ID already exists.\n";
        continue;
    }
    cin.ignore();
    cout << "Enter name: ";
    getline(cin, name);
    cout << "Enter stream: ";
    getline(cin, stream);

    students[sid] = {name, sid, stream};
    cout << "Account created. You can now log in.\n";
}
cout << "Enter your Student ID to login: ";
cin >> sid;
if (!students.count(sid)) {
    cout << "Invalid student ID.\n";
    continue;
}


            Student& stu = students[sid];
            int stuChoice;
            while (true) {
                cout << "\n1. Issue Book\n2. Return Book\n3. Back\nEnter choice: ";
                cin >> stuChoice;
                if (stuChoice == 3) break;
                if (stuChoice == 1) {
                    if (stu.issuedBooks.size() >= 2) {
                        cout << "Cannot issue more than 2 books.\n";
                        continue;
                    }
                    string book;
                    cout << "Enter book to issue: ";
                    cin >> book;
                    if (!books.count(book) || books[book].availableQuantity <= 0) {
                        cout << "Book not available.\n";
                        continue;
                    }

                    time_t now = time(0);
                    time_t due = now + 14*60*60*24; // 14 weeks 

                    stu.issuedBooks.push_back({book, now, due});
                    books[book].availableQuantity--;
                    printTime("Issued at: ", now);
                    printTime("Due at   : ", due);
                } else if (stuChoice == 2) {
                    string book;
                    cout << "Enter book to return: ";
                    cin >> book;
                    bool found = false;
                    for (auto it = stu.issuedBooks.begin(); it != stu.issuedBooks.end(); ++it) {
                        if (it->bookName == book) {
                            found = true;
                            time_t now = time(0);
                            printTime("Returned at: ", now);
                            printTime("Due time   : ", it->dueTime);
                            if (now > it->dueTime) {
                                int secondsLate = difftime(now, it->dueTime);
                                int fine = (secondsLate/(60*60*24)) * 5;
                                cout << "Late by " << secondsLate << " seconds. Fine: Rs. " << fine << endl;
                            } else {
                                cout << "Returned on time. No fine.\n";
                            }
                            books[book].availableQuantity++;
                            stu.issuedBooks.erase(it);
                            break;
                        }
                    }
                    if (!found) {
                        cout << "Book not issued.\n";
                    }
                }
            }
        } else {
            break;
        }
    }
    saveBooks(books);
    saveStudents(students);
    
    return 0;
}
