from flask import Flask, request, redirect, url_for

app = Flask(__name__)

items = [
    {"name": "Black Water Bottle", "category": "Bottle", "status": "Reported"},
    {"name": "Engineering Notebook", "category": "Books", "status": "Found"}
]

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CampusVault - Lost & Found</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial; margin: 40px auto; max-width: 800px;
                   padding: 20px; background: #f2f5fa; color: #222; }
            h1 { color: #244b85; }
            .card { background: white; padding: 16px; margin: 12px 0;
                    border-radius: 10px; box-shadow: 0 2px 6px #ddd; }
            input, select, button { padding: 10px; margin: 5px 0;
                    width: 100%; box-sizing: border-box; }
            button { background: #244b85; color: white; border: 0;
                     border-radius: 5px; cursor: pointer; }
            .status { color: #247347; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>CampusVault</h1>
        <p>College Lost & Found Management System</p>
        <div class="card">
            <h2>Report an Item</h2>
            <form action="/add" method="post">
                <input name="name" placeholder="Item name" required>
                <input name="category" placeholder="Category" required>
                <select name="status">
                    <option>Lost</option>
                    <option>Found</option>
                </select>
                <button type="submit">Add Item</button>
            </form>
        </div>
        <h2>Reported Items</h2>
        {%ITEMS%}
        <p>CampusVault | Flask CI/CD Project</p>
    </body>
    </html>
    """
    cards = ""
    for item in items:
        cards += (
            '<div class="card"><h3>' + item["name"] + '</h3>'
            '<p>Category: ' + item["category"] + '</p>'
            '<p>Status: <span class="status">' + item["status"] + '</span></p>'
            '</div>'
        )
    return html.replace("{%ITEMS%}", cards)

@app.route("/add", methods=["POST"])
def add_item():
    name = request.form.get("name", "").strip()
    category = request.form.get("category", "").strip()
    status = request.form.get("status", "Lost")
    if name and category:
        items.append({
            "name": name,
            "category": category,
            "status": status
        })
    return redirect(url_for("home"))

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)