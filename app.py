from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    ambassadors = [
        {"name": "JAGAT SARKAR", "img": "BA3.jpeg"},
        {"name": "VIVEK SHELAR", "img": "BA1.jpeg"},
        {"name": "SARFARAZ BAHUBALI", "img": "BA.jpeg"}
    ]
    gallery = [
        {"img": "sachin.jpeg", "title": "sachin sir in our jersy"},
        {"img": "sachin2.jpeg", "title": "Sachin Sir with Elite Series"},
        {"img": "sachin3.jpeg", "title": "Legacy of 7070 Sports"}
    ]
    return render_template('index.html', page="home", ambassadors=ambassadors, gallery=gallery)

@app.route('/bats')
def bats():
    # Final List: Sachin Sir ki photo yahan se hatai gayi hai
    all_bats = [
        {"name": "Kashmir Willow Edition", "price": "₹3,500", "img": "WhatsApp Image 2026-01-26 at 10.32.14 PM.jpeg"},
        {"name": "Limited Edition G1", "price": "₹5,500", "img": "WhatsApp Image 2026-01-26 at 10.32.15 PM.jpeg"},
        {"name": "Pro Series G2", "price": "₹4,200", "img": "WhatsApp Image 2026-01-26 at 10.32.16 PM.jpeg"},
        {"name": "Gold Edition Pro", "price": "₹6,000", "img": "WhatsApp Image 2026-01-26 at 10.32.18 PM.jpeg"},
        {"name": "Master Blaster G1", "price": "₹4,800", "img": "WhatsApp Image 2026-01-26 at 10.32.20 PM.jpeg"},
        {"name": "Player Edition G1", "price": "₹7,500", "img": "WhatsApp Image 2026-01-26 at 10.32.21 PM.jpeg"},
        {"name": "Junior Pro Series", "price": "₹2,500", "img": "WhatsApp Image 2026-01-26 at 10.32.21 PM (1).jpeg"},
        {"name": "Power Hitter G3", "price": "₹3,800", "img": "WhatsApp Image 2026-01-26 at 10.32.24 PM.jpeg"},
        {"name": "Tournament Special", "price": "₹5,200", "img": "WhatsApp Image 2026-01-26 at 10.32.24 PM (1).jpeg"},
        {"name": "Dynamic G3 Willow", "price": "₹4,100", "img": "WhatsApp Image 2026-01-26 at 10.32.25 PM.jpeg"},
        {"name": "Elite Willow Pro", "price": "₹8,000", "img": "WhatsApp Image 2026-01-26 at 10.32.25 PM (1).jpeg"},
        {"name": "Club Classic Edition", "price": "₹3,300", "img": "WhatsApp Image 2026-01-26 at 10.32.26 PM.jpeg"},
        {"name": " Super Power 7070", "price": "₹4,600", "img": "WhatsApp Image 2026-01-26 at 10.32.32 PM.jpeg"},
        {"name": "Blast G1 Edition", "price": "₹5,900", "img": "WhatsApp Image 2026-01-26 at 10.32.30 PM (3).jpeg"},
        {"name": "7070 Grand Slam G1","price":"₹3,900","img":"WhatsApp Image 2026-01-26 at 10.32.29 PM (2).jpeg"},
    ]
    return render_template('index.html', page="bats", bats=all_bats)

if __name__ == '__main__':
    app.run(debug=True)