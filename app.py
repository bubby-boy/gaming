
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

GAMES = [
    {
        "id": "eaglercraft",
        "name": "Eaglercraft",
        "category": "Sandbox",
        "description": "Minecraft-inspired block building in your browser.",
        "emoji": "⛏️",
        "style": "minecraft",
        "url": "https://eaglercraft.com/"
    },
    {
        "id": "miniblox",
        "name": "Miniblox",
        "category": "Sandbox",
        "description": "Explore voxel worlds and play building games.",
        "emoji": "🧱",
        "style": "voxel",
        "url": "https://miniblox.io/"
    },
    {
        "id": "bloxd",
        "name": "Bloxd.io",
        "category": "Sandbox",
        "description": "Blocky worlds, parkour, creative modes and more.",
        "emoji": "🌎",
        "style": "arcade",
        "url": "https://bloxd.io/"
    },
    {
        "id": "minecraft-classic",
        "name": "Minecraft Classic",
        "category": "Sandbox",
        "description": "Build in the classic creative Minecraft experience.",
        "emoji": "🌲",
        "style": "minecraft",
        "url": "https://classic.minecraft.net/"
    },
    {
        "id": "crazygames",
        "name": "CrazyGames",
        "category": "Arcade",
        "description": "A large collection of games across many genres.",
        "emoji": "🎮",
        "style": "action",
        "url": "https://www.crazygames.com/"
    },
    {
        "id": "itch",
        "name": "itch.io HTML5",
        "category": "Indie",
        "description": "Discover indie games playable in a browser.",
        "emoji": "🕹️",
        "style": "puzzle",
        "url": "https://itch.io/games/html5"
    },
    {
        "id": "poki",
        "name": "Poki",
        "category": "Arcade",
        "description": "Free-to-play games for quick gaming sessions.",
        "emoji": "✨",
        "style": "racing",
        "url": "https://poki.com/"
    },
    {
        "id": "kongregate",
        "name": "Kongregate",
        "category": "Arcade",
        "description": "Browse web games and indie favorites.",
        "emoji": "🏆",
        "style": "arcade",
        "url": "https://www.kongregate.com/"
    }
]


@app.route("/")
def index():
    return render_template("index.html", games=GAMES)


@app.route("/api/games")
def api_games():
    query = request.args.get("q", "").strip().lower()
    category = request.args.get("category", "All")

    results = []

    for game in GAMES:
        if category != "All" and game["category"] != category:
            continue

        searchable = (
            game["name"] + " " +
            game["category"] + " " +
            game["description"]
        ).lower()

        if query and query not in searchable:
            continue

        results.append(game)

    return jsonify(results)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
