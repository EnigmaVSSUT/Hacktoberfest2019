using System;

namespace CodeConsole.CodeEditor {
    public partial class CliEditor {
        /// <summary>
        ///     A wrapper over <see cref="Console.CursorLeft" />.
        ///     Position is relative to <see cref="editBoxPoint" />.
        ///     Automatically grows or reduces <see cref="Console.BufferWidth" />
        ///     based on longest line length.
        /// </summary>
        private int cursorX {
            // check that value is in bounds
            get => Console.CursorLeft - editBoxPoint.X;
            set => Console.CursorLeft = value + editBoxPoint.X;
        }

        /// <summary>
        ///     A wrapper over <see cref="Console.CursorTop" />.
        ///     Position is relative to <see cref="editBoxPoint" />.
        /// </summary>
        private int cursorY {
            get => Console.CursorTop - editBoxPoint.Y;
            set => Console.CursorTop = value + editBoxPoint.Y;
        }
        
        private void MoveToNextLineStart() {
            cursorY++;
            if (cursorY == lines.Count) {
                try {
                    ClearLine();
                }
                catch (FileTooLargeException ex) {
                    EditorHeader = ex.Message;
                }
            }

            cursorX = 0;
        }
        
        private bool HandleEditAction(ConsoleKeyInfo key) {
            switch (key.Key) {
            case ConsoleKey.Escape: {
                // use [Enter] in single line mode instead.
                if (settings.SingleLineMode) {
                    break;
                }

                key = Console.ReadKey(true);
                if (key.Key == ConsoleKey.Escape) {
                    return true;
                }

                break;
            }

            case ConsoleKey.Enter: {
                if (settings.SingleLineMode) {
                    return true;
                }

                SplitLine();
                break;
            }

            case ConsoleKey.Backspace: {
                EraseLeftChar();
                break;
            }

            case ConsoleKey.Delete: {
                EraseRightChar();
                break;
            }

            case ConsoleKey.Tab: {
                // Shift + Tab: outdent current tab
                if (key.Modifiers == ConsoleModifiers.Shift
                    && Line.StartsWith(settings.Tabulation)) {
                    Line = Line.Remove(0, settings.Tabulation.Length);
                }
                // if on the left side of cursor there are only whitespaces
                else if (string.IsNullOrWhiteSpace(Line.Substring(0, cursorX))) {
                    cursorX += settings.Tabulation.Length;
                    Line    =  settings.Tabulation + lines[cursorY];
                }
                else {
                    WriteValue(' ');
                }

                break;
            }

            case ConsoleKey.Insert: {
                // do not process insert key
                break;
            }

            // TODO (UI) add something for FN keys
            case ConsoleKey.F1:
            case ConsoleKey.F2:
            case ConsoleKey.F3:
            case ConsoleKey.F4:
            case ConsoleKey.F5:
            case ConsoleKey.F6:
            case ConsoleKey.F7:
            case ConsoleKey.F8:
            case ConsoleKey.F9:
            case ConsoleKey.F10:
            case ConsoleKey.F11:
            case ConsoleKey.F12: {
                break;
            }

            // any other char that should be passed in code
            default: {
                WriteValue(key.KeyChar);
                break;
            }
            }

            return false;
        }

        private bool HandleViewAction(ConsoleKeyInfo key) {
            var isViewFunction = true;
            switch (key.Key) {
            #region Move cursor with arrows

            case ConsoleKey.LeftArrow:
            case ConsoleKey.RightArrow:
            case ConsoleKey.UpArrow:
            case ConsoleKey.DownArrow: {
                MoveCursor(key.Key);
                break;
            }

            #endregion

            case ConsoleKey.Home: {
                // to line start
                cursorX = 0;
                break;
            }

            case ConsoleKey.End: {
                // to line end
                cursorX = Line.Length;
                break;
            }

            case ConsoleKey.PageUp: {
                if (cursorY - 10 >= 0) {
                    cursorY -= 10;
                }
                else {
                    cursorY = 0;
                }

                if (cursorX > Line.Length) {
                    cursorX = Line.Length;
                }

                break;
            }

            case ConsoleKey.PageDown: {
                if (cursorY + 10 < lines.Count) {
                    cursorY += 10;
                }
                else {
                    cursorY = lines.Count - 1;
                }

                if (cursorX > Line.Length) {
                    cursorX = Line.Length;
                }

                break;
            }

            default: {
                isViewFunction = false;
                break;
            }
            }

            return isViewFunction;
        }
        
        
        /// <summary>
        ///     Moves cursor in edit box to specified <see cref="direction" />.
        /// </summary>
        /// <param name="direction">Direction of cursor move.</param>
        /// <param name="count">Count of characters to move cursor by.</param>
        private void MoveCursor(ConsoleKey direction, int count = 1) {
            switch (direction) {
            case ConsoleKey.LeftArrow: {
                // if reach first line start
                if (cursorY == 0
                    && cursorX - count < 0) {
                    return;
                }

                // if fits in current line
                if (cursorX - count >= 0) {
                    cursorX -= count;
                }
                // move line up
                else if (!settings.SingleLineMode) {
                    cursorY--;
                    cursorX = Line.Length; // no - 1
                }

                break;
            }

            case ConsoleKey.RightArrow: {
                // if reach last line end
                if (cursorY == lines.Count - 1
                    && cursorX + count > Line.Length) {
                    return;
                }

                // if fits in current line
                if (cursorX + count <= Line.Length) {
                    cursorX += count;
                }
                // move line down
                else if (!settings.SingleLineMode) {
                    cursorY++;
                    cursorX = 0;
                }

                break;
            }

            case ConsoleKey.UpArrow: {
                // if on first line
                if (cursorY == 0 || settings.SingleLineMode) {
                    return;
                }

                cursorY--;
                // if cursor moves at empty space upside
                if (cursorX >= Line.Length) {
                    cursorX = Line.Length;
                }

                break;
            }

            case ConsoleKey.DownArrow: {
                // if on last line
                if (cursorY == lines.Count - 1 || settings.SingleLineMode) {
                    return;
                }

                cursorY++;
                // if cursor moves at empty space downside
                if (cursorX >= Line.Length) {
                    cursorX = Line.Length;
                }

                break;
            }
            }
        }
    }
}