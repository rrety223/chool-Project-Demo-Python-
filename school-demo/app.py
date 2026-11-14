"""Riverside High School demo website (Flask)."""
import re

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
# Demo only. Replace with a secret loaded from an environment variable in production.
app.config["SECRET_KEY"] = "dev-only-change-me"

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

SCHOOL = {
    "name": "Riverside High School",
    "motto": "Learn. Create. Lead.",
    "address": "123 Maple Avenue, Springfield",
    "phone": "+1 (555) 010-2030",
    "email": "info@riverside-hs.example",
    "hours": "Monday to Friday, 8:00 AM - 4:30 PM",
}

PROGRAMS = [
    {
        "title": "Mathematics",
        "description": "From algebra to calculus, with a strong focus on problem solving and real-world applications.",
        "icon": "∑",
    },
    {
        "title": "Science",
        "description": "Hands-on labs in biology, chemistry and physics, plus an annual science fair.",
        "icon": "⚗",
    },
    {
        "title": "Languages & Literature",
        "description": "English literature, creative writing and two world languages taught from Grade 9.",
        "icon": "✎",
    },
    {
        "title": "Arts & Design",
        "description": "Painting, digital design, music and drama, with a student exhibition every spring.",
        "icon": "◐",
    },
    {
        "title": "Computer Science",
        "description": "Programming, web development and robotics in a fully equipped computer lab.",
        "icon": "</>",
    },
    {
        "title": "Sports & Wellness",
        "description": "Team sports, athletics and physical education that supports both body and mind.",
        "icon": "⚽",
    },
]

FACULTY = [
    {"name": "Dr. Emily Carter", "role": "Principal", "subject": "Educational Leadership"},
    {"name": "James Ollins", "role": "Head of Mathematics", "subject": "Mathematics"},
    {"name": "Dr. Priya Shah", "role": "Head of Science", "subject": "Chemistry"},
    {"name": "Laura Mendes", "role": "Head of Languages", "subject": "English Literature"},
    {"name": "Samuel Brooks", "role": "Head of Arts", "subject": "Visual Arts"},
    {"name": "Kenji Watanabe", "role": "Computer Science Teacher", "subject": "Programming"},
]

NEWS = [
    {
        "date": "2025-09-02",
        "title": "Welcome back, students!",
        "summary": "The new school year starts with three new clubs and an upgraded library.",
    },
    {
        "date": "2025-09-15",
        "title": "Robotics team qualifies for regionals",
        "summary": "Our robotics team placed second at the district qualifier and advances to the regional finals.",
    },
    {
        "date": "2025-10-03",
        "title": "Open House on October 18",
        "summary": "Prospective families are invited to tour classrooms and meet our teachers.",
    },
]

# In-memory storage for contact messages. Data is lost when the server restarts.
contact_messages = []


@app.context_processor
def inject_globals():
    """Make school info and the current endpoint available to every template."""
    return {"school": SCHOOL, "current_endpoint": request.endpoint}


@app.route("/")
def index():
    return render_template("index.html", programs=PROGRAMS[:3], news=NEWS[:2])


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/programs")
def programs():
    return render_template("programs.html", programs=PROGRAMS)


@app.route("/faculty")
def faculty():
    return render_template("faculty.html", faculty=FACULTY)


@app.route("/admissions")
def admissions():
    return render_template("admissions.html")


@app.route("/news")
def news():
    return render_template("news.html", news=NEWS)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = {"name": "", "email": "", "message": ""}

    if request.method == "POST":
        form["name"] = request.form.get("name", "").strip()
        form["email"] = request.form.get("email", "").strip()
        form["message"] = request.form.get("message", "").strip()

        errors = []
        if not form["name"]:
            errors.append("Please enter your name.")
        if not EMAIL_RE.match(form["email"]):
            errors.append("Please enter a valid email address.")
        if not form["message"]:
            errors.append("Please write a message.")
        elif len(form["message"]) > 2000:
            errors.append("Your message must be 2000 characters or fewer.")

        if errors:
            for error in errors:
                flash(error, "error")
        else:
            contact_messages.append(dict(form))
            flash("Thank you! Your message has been sent. We will reply within two business days.", "success")
            return redirect(url_for("contact"))

    return render_template("contact.html", form=form)


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
