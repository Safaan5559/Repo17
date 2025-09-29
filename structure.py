NumberGuessGame/
│
├── main.py             # Entry point: initializes player, UI, and game loop
├── settings.py         # Game settings: min/max numbers, max attempts, difficulties
├── player.py           # Player class: name, score, attempts
├── game.py             # Core game logic: guessing, checking, scoring
├── ui.py               # User Interface: menus, messages, input handling
├── hints.py            # Hint system: provide clues based on guesses
├── history.py          # Game history: store previous games, high scores
├── achievements.py     # Achievements/unlocks system
├── leaderboard.py      # Global/local leaderboard tracking
├── utils.py            # Utility functions: validation, random generation
│
├── resources/          # All images, sounds, and fonts
│   ├── images/
│   │   ├── logo.png
│   │   ├── background.png
│   │   └── icons/
│   ├── sounds/
│   │   ├── correct.wav
│   │   └── wrong.wav
│   └── fonts/
│       └── arcade.ttf
│
├── data/               # Persistent data storage (JSON, CSV)
│   ├── scores.json
│   ├── history.json
│   └── settings.json
│
├── levels/             # Optional: difficulty or stage files
│   ├── easy.py
│   ├── medium.py
│   └── hard.py
│
├── screens/            # UI screens for Kivy/GUI
│   ├── main_menu.py
│   ├── game_screen.py
│   ├── settings_screen.py
│   └── leaderboard_screen.py
│
├── buildozer.spec      # Buildozer configuration for APK
└── README.md           # Project overview, instructions