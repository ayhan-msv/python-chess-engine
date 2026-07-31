Chess Game with AI Opponent
A fully playable chess application built in Python using Pygame for graphics and a classic minimax + alpha-beta pruning AI engine. It supports both two-player local matches and single-player games against the computer, where you can choose to play as white or black.

Architecture
The project is cleanly separated into distinct modules, each with a focused responsibility:

main.py — The entry point and game loop. Handles Pygame initialization, rendering the board and pieces, highlighting valid moves, processing mouse clicks, and detecting end-game states. Keyboard shortcuts let you reset (r) or undo (u) moves.

chess_engine.py — The heart of the game. The game_state class tracks the board, whose turn it is, move history, and captured pieces. It implements the full rules of chess: legal move generation, check/checkmate/stalemate detection, castling, en passant, pawn promotion, pins, and move undo via a chess_move history log.

Piece.py — An object-oriented piece hierarchy. A base Piece class is extended by Rook, Knight, Bishop, Queen, King, and Pawn, each defining its own movement and capture logic. Queen cleverly reuses Rook and Bishop behavior through multiple inheritance.

ai_engine.py — The chess_ai class implements the minimax algorithm with alpha-beta pruning to a depth of 3. Separate routines handle the AI playing white or black, using a material-based board evaluation that scores pieces (king 1000, queen 100, rook 50, bishop/knight 30, pawn 10).

enums.py — Shared constants defining players (white/black), empty squares, and piece identifiers used for loading images.

Key Features
Complete rule enforcement including special moves (castling, en passant, promotion).
Sophisticated check detection that identifies checking pieces, pinned pieces, and legal responses.
Visual move highlighting and a graphical board rendered from piece images.
An adjustable-difficulty AI that searches ahead and prunes suboptimal branches for efficiency.
A solid demonstration of game-state management, object-oriented design, and adversarial search in a real, interactive application.
