# 0x00. Pagination

## Project Overview
This project introduces the concept of pagination in web applications. You will implement server-side pagination for a dataset, enabling efficient data retrieval and navigation for large collections.

## Learning Objectives
- Understand the need for pagination in web APIs and applications.
- Implement server-side pagination logic.
- Design endpoints that support paginated responses.
- Handle edge cases (e.g., out-of-range pages, invalid parameters).

## Requirements
- Python 3.x
- Flask (for API demonstration)
- Any additional dependencies listed in `requirements.txt`

## Project Structure
- `server.py` – Main Flask server implementing pagination endpoints.
- `dataset.csv` – Example dataset used for pagination.
- `README.md` – Project documentation.
- `tests/` – Unit and integration tests for pagination logic.

## Usage
1. Install dependencies:
   ```zsh
   pip install -r requirements.txt
   ```
2. Run the server:
   ```zsh
   python server.py
   ```
3. Access the API at `http://localhost:5000/` and use the pagination endpoints.

## Example API Usage
To retrieve items 11–20 from the dataset, use:
```
GET /api/v1/items?page=2&page_size=10
```
This returns the second page of results, with 10 items per page.

## References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pagination Concepts](https://en.wikipedia.org/wiki/Pagination)

