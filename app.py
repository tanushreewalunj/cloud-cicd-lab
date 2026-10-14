
from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Sample lost and found items
items = [
    {
        "name": "Black Water Bottle",
        "category": "Bottle",
        "status": "Reported"
    },
    {
        "name": "Engineering Notebook",
        "category": "Books",
        "status": "Found"
    }
]

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CampusVault - Lost & Found</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            margin: 40px auto;
            max-width: 800px;
            padding: 20px;
            background: #f2f5fa;
            color: #222;
        }

        h1 {
            color: #244b85;
            text-align: center;
        }

        .subtitle {
            text-align: center;
            color: #555;
        }

        .card {
            background: white;
            padding: 18px;
            margin: 12px 0;
            border-radius: 10px;
            box-shadow: 0 2px 6px #ddd;
            overflow-wrap: anywhere;
        }

        input, select, button {
            padding: 12px;
            margin: 7px 0;
            width: 100%;
            box-sizing: border-box;
            border-radius: 5px;
            font-size: 15px;
        }

        input, select {
            border: 1px solid #ccc;
            background: white;
        }

        button {
            background: #244b85;
            color: white;
            border: 0;
            cursor: pointer;
        }

        button:hover {
            background: #183765;
        }

        .status {
            color: #247347;
            font-weight: bold;
        }

        .badge {
            display: inline-block;
            background: #e8effb;
            color: #244b85;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 13px;
        }

        footer {
            text-align: center;
            margin-top: 30px;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>

<body>
    <h1>CampusVault</h1>
    <p class="subtitle">
        College Lost & Found Management System
    </p>

    <div class="card">
        <h2>Report an Item</h2>

        <form action="/add" method="post">
            <label for="name">Item Name</label>
            <input
                id="name"
                name="name"
                placeholder="Enter item name"
                maxlength="100"
                required
            >

            <label for="category">Category</label>
            <input
                id="category"
                name="category"
                placeholder="Bottle, Books, Electronics..."
                maxlength="60"
                required
            >

            <label for="status">Item Status</label>
            <select id="status" name="status">
                <option value="Lost">Lost</option>
                <option value="Found">Found</option>
                <option value="Reported">Reported</option>
            </select>

            <button type="submit">Add Item</button>
        </form>
    </div>

    <h2>Reported Items</h2>

    {% if items %}
        {% for item in items %}
            <div class="card">
                <h3>{{ item.name }}</h3>
                <p>
                    <strong>Category:</strong>
                    {{ item.category }}
                </p>
                <p>
                    <strong>Status:</strong>
                    <span class="status">{{ item.status }}</span>
                </p>
                <span class="badge">Campus Lost & Found</span>
            </div>
        {% endfor %}
    {% else %}
        <div class="card">
            <p>No items reported yet.</p>
        </div>
    {% endif %}

    <footer>
        <p>CampusVault | Flask CI/CD Project</p>
        <p>Version 3 - Automatic Deployment Successful</p>
    </footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_PAGE, items=items)


@app.route("/add", methods=["POST"])
def add_item():
    name = request.form.get("name", "").strip()
    category = request.form.get("category", "").strip()
    status = request.form.get("status", "Lost").strip()

    allowed_statuses = {"Lost", "Found", "Reported"}

    if (
        name
        and category
        and len(name) <= 100
        and len(category) <= 60
        and status in allowed_statuses
    ):
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
