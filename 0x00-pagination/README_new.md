# 0x00. Pagination

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/REST-API-0052CC?style=for-the-badge" alt="REST API">
</p>

<div align="center">
  <h3>📄 Master Efficient Data Pagination</h3>
  <p><em>Build scalable APIs that handle large datasets with optimal performance</em></p>
</div>

---

## 🎯 Overview

This project introduces the fundamental concepts of **pagination** in web applications and APIs. You'll learn to implement server-side pagination strategies that enable efficient data retrieval and navigation for large datasets.

**Real-world Applications:** Social media feeds, e-commerce catalogs, search results, database optimization

## 📚 Project Tasks

| Task | File | Description |
|------|------|-------------|
| **0** | `0-simple_helper_function.py` | Implement `index_range` function for pagination calculations |
| **1** | `1-simple_pagination.py` | Create `Server` class with basic pagination functionality |
| **2** | `2-hypermedia_pagination.py` | Extend pagination with hypermedia metadata and navigation |
| **3** | `3-hypermedia_del_pagination.py` | Handle deletion-resilient pagination for dynamic datasets |

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- CSV dataset (Popular_Baby_Names.csv provided)

### Quick Start
```bash
# Run individual tasks
python3 0-main.py  # Test index range function
python3 1-main.py  # Basic pagination
python3 2-main.py  # Hypermedia pagination
python3 3-main.py  # Deletion-resilient pagination

# Test your implementations
python3 -m pytest  # If tests are available
```

### Usage Example
```python
# Basic pagination
server = Server()
page_data = server.get_page(page=1, page_size=10)

# Hypermedia pagination
pagination_info = server.get_hyper(page=2, page_size=15)
print(pagination_info['next_page'])  # Navigation info
```

## 📚 Documentation

For detailed information, see:
- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System design and implementation details
- **[PROJECT-MANIFEST.md](./PROJECT-MANIFEST.md)** - Learning objectives and competencies

## 📖 Key Concepts

- **Server-side Pagination**: Efficient data chunking for large datasets
- **Hypermedia APIs**: Self-describing APIs with navigation metadata
- **Edge Case Handling**: Robust pagination for invalid inputs
- **Performance Optimization**: Memory-efficient data retrieval

## 🔧 Implementation Notes

- Handle `page` and `page_size` parameters properly
- Validate input ranges and provide meaningful defaults
- Include comprehensive error handling for edge cases
- Follow RESTful API design principles

---

**Learning Objective**: Master pagination fundamentals for scalable backend systems
