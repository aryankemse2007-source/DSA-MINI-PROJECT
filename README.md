# Student Record Management System (DSA Mini Project)

A CLI-based Student Record Management System implemented in Python, utilizing standard Data Structures and Algorithms for optimized search, sort, and storage operations.

## Key DSA Implementations
- **Data Structure**: Dynamic Array of Dictionaries / Hash Maps for in-memory record storage.
- **Search Algorithm**: Binary Search (O(log n)) for fast lookup by Roll Number.
- **Sorting Algorithm**: Merge Sort (O(n log n)) applied for generating merit rankings and ordering roll numbers.
- **Persistence**: File I/O using JSON serialization (`records.json`).

## Complexity Analysis
| Operation | Algorithm | Time Complexity | Space Complexity |
|---|---|---|---|
| Search (Roll No) | Binary Search | O(log n) | O(1) |
| Sorting (Merit/Roll) | Merge Sort | O(n log n) | O(n) |
| Insertion | Append | O(1) amortized | O(1) |
| Deletion | Linear Lookup + Shift | O(n) | O(1) |

## Project Files
- `main.py`: Complete source code with menu-driven interface, Merge Sort, and Binary Search.
- `records.json`: Local database file storing student data persistently.
- `README.md`: Documentation and algorithmic complexity breakdown.

## How to Run
```bash
python main.py
```
