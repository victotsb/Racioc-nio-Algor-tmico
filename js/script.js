document.addEventListener("DOMContentLoaded", () => {

    const moveSound = new Audio('move.mp3');
    const mergeSound = new Audio('merge.mp3');
    const gameOverSound = new Audio('game-over.mp3');

    const Game = {
        size: 4,
        grid: [],
        score: 0,
        bestScore: Number(localStorage.getItem("bestScore")) || 0,
        difficulty: "medium",

        init() {
            this.grid = Array(this.size * this.size).fill(0);
            this.score = 0;
            this.spawn();
            this.spawn();
            UI.hideGameOver();
            UI.render();
        },

        spawn() {
            const empty = this.grid
                .map((v, i) => v === 0 ? i : null)
                .filter(v => v !== null);

            if (!empty.length) return null;

            const index = empty[Math.floor(Math.random() * empty.length)];

            const spawnRates = {
                easy:  { 2: 0.95, 4: 0.05 },
                medium:{ 2: 0.9,  4: 0.1 },
                hard:  { 2: 0.7,  4: 0.25, 8: 0.05 }
            };

            const rates = spawnRates[this.difficulty];
            const rand = Math.random();
            let cumulative = 0;

            for (let value in rates) {
                cumulative += rates[value];
                if (rand <= cumulative) {
                    this.grid[index] = Number(value);
                    return index;
                }
            }

            return null;
        },

        move(direction) {
            let moved = false;
            let mergedThisTurn = false;

            for (let i = 0; i < this.size; i++) {
                const line = this.getLine(i, direction);
                const { newLine, merged } = this.merge(line);

                const changed = line.some((v, idx) => v !== newLine[idx]);

                if (changed) {
                    moved = true;
                    if (merged) mergedThisTurn = true;
                    this.setLine(i, direction, newLine);
                }
            }

            if (moved) {
                moveSound.play();
                if (mergedThisTurn) mergeSound.play();

                const spawnedIndex = this.spawn();
                UI.render(spawnedIndex);

                if (this.isGameOver()) {
                    UI.showGameOver();
                    gameOverSound.play();
                }
            }
        },

        merge(line) {
            const filtered = line.filter(v => v !== 0);
            let merged = false;

            for (let i = 0; i < filtered.length - 1; i++) {
                if (filtered[i] === filtered[i + 1]) {
                    filtered[i] *= 2;
                    this.score += filtered[i];
                    filtered[i + 1] = 0;
                    merged = true;
                }
            }

            const newLine = filtered
                .filter(v => v !== 0)
                .concat(Array(this.size).fill(0))
                .slice(0, this.size);

            return { newLine, merged };
        },

        getLine(i, direction) {
            const line = [];

            for (let j = 0; j < this.size; j++) {
                let index;

                if (direction === "left") index = i * this.size + j;
                if (direction === "right") index = i * this.size + (this.size - 1 - j);
                if (direction === "up") index = j * this.size + i;
                if (direction === "down") index = (this.size - 1 - j) * this.size + i;

                line.push(this.grid[index]);
            }

            return line;
        },

        setLine(i, direction, line) {
            for (let j = 0; j < this.size; j++) {
                let index;

                if (direction === "left") index = i * this.size + j;
                if (direction === "right") index = i * this.size + (this.size - 1 - j);
                if (direction === "up") index = j * this.size + i;
                if (direction === "down") index = (this.size - 1 - j) * this.size + i;

                this.grid[index] = line[j];
            }
        },

        isGameOver() {
            if (this.grid.includes(0)) return false;

            for (let i = 0; i < this.size; i++) {
                for (let j = 0; j < this.size; j++) {
                    const index = i * this.size + j;
                    const value = this.grid[index];

                    if (j < this.size - 1 && value === this.grid[index + 1]) return false;
                    if (i < this.size - 1 && value === this.grid[index + this.size]) return false;
                }
            }

            return true;
        }
    };

    const UI = {
        cells: [],
        board: document.getElementById("game-board"),
        scoreElement: document.getElementById("score"),
        bestScoreElement: document.getElementById("best-score"),
        gameOverElement: document.getElementById("game-over"),

        init() {
            this.board.innerHTML = "";
            this.cells = [];

            for (let i = 0; i < Game.size * Game.size; i++) {
                const cell = document.createElement("div");
                cell.classList.add("cell");
                this.board.appendChild(cell);
                this.cells.push(cell);
            }
        },

        render(spawnedIndex = null) {
            this.cells.forEach((cell, index) => {
                const value = Game.grid[index];

                cell.textContent = value || "";
                cell.dataset.value = value || "";
                cell.classList.remove("spawn");

                if (index === spawnedIndex) {
                    cell.classList.add("spawn");
                    setTimeout(() => {
                        cell.classList.remove("spawn");
                    }, 250);
                }
            });

            this.scoreElement.textContent = Game.score;

            if (Game.score > Game.bestScore) {
                Game.bestScore = Game.score;
                localStorage.setItem("bestScore", Game.bestScore);
            }

            this.bestScoreElement.textContent = Game.bestScore;
        },

        showGameOver() {
            this.gameOverElement.style.display = "block";
        },

        hideGameOver() {
            this.gameOverElement.style.display = "none";
        }
    };

    UI.init();
    Game.init();

    document.addEventListener("keydown", e => {
        const keys = {
            ArrowUp: "up",
            ArrowDown: "down",
            ArrowLeft: "left",
            ArrowRight: "right",
            w: "up",
            s: "down",
            a: "left",
            d: "right"
        };
        if (keys[e.key]) Game.move(keys[e.key]);
    });

    document.getElementById("restart-btn")
        .addEventListener("click", () => Game.init());

    document.getElementById("difficulty")
        .addEventListener("change", e => {
            Game.difficulty = e.target.value;
            Game.init();
        });

    document.getElementById("theme")
        .addEventListener("change", e => {
            document.body.classList.toggle("theme-dark", e.target.value === "dark");
        });

});