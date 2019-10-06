using System;
using System.Collections.Generic;
using System.Drawing;

namespace CodeConsole.CodeEditor {
    public partial class CliEditor {
        private static List<Exception> blames;
        private        int             lastRenderLinesCount;
        private        Point           newRenderStartPosition;
        
        /// <summary>
        ///     Editor area top-left position in console.
        /// </summary>
        private Point editBoxPoint;

        /// <summary>
        ///     (X, Y) position of editor's header.
        ///     (works only with syntax highlighting
        ///     and in multiline mode).
        /// </summary>
        private Point headerPoint;

        private string EditorHeader {
            set {
                ConsoleUI.WithPosition(
                    headerPoint,
                    () => {
                        ConsoleUI.ClearLine(2);
                        if (string.IsNullOrWhiteSpace(value)) {
                            Console.Write(CliEditorSettings.DefaultHeader);
                        }
                        else {
                            ConsoleUI.Write(
                                (value,
                                 value.ToUpper().StartsWith("ERROR")
                                     ? ConsoleColor.Red
                                     : ConsoleColor.Yellow)
                            );
                        }
                    }
                );
            }
        }

        /// <summary>
        ///     Full rewriting and highlighting of current code.
        /// </summary>
        private void RenderCode() {
            int linesCountDifference = lines.Count - lastRenderLinesCount;
            ConsoleUI.WithCurrentPosition(
                () => {
                    if (settings.SyntaxHighlighting) {
                        HighlightSyntax();
                    }
                    else if (!settings.SingleLineMode && linesCountDifference != 0) {
                        // rewrite all lines from cursor
                        for (; cursorY < lines.Count; cursorY++) {
                            ClearLine();
                            Console.Write(Line);
                        }
                    }
                    else {
                        ClearLine();
                        Console.Write(Line);
                    }

                    // if line arrived
                    if (linesCountDifference > 0) {
                        // change line numbers below
                        cursorY            = lines.Count - 1;
                        Console.CursorLeft = 0;
                        DrawCurrentLineNumber();
                        linesCountDifference--;
                    }
                    // if line removed
                    else if (linesCountDifference < 0) {
                        // clear last line
                        cursorY = lastRenderLinesCount - 1;
                        ClearLine(true);
                        linesCountDifference++;
                    }
                }
            );
            lastRenderLinesCount = lines.Count;
        }

        private void HighlightSyntax() {
            List<ColoredValue> values = settings.Highlighter.Highlight(
                lines,
                ref newRenderStartPosition,
                out blames
            );

            cursorX = newRenderStartPosition.X;
            cursorY = newRenderStartPosition.Y;
            ClearLines(cursorX, cursorY);

            foreach (ColoredValue value in values) {
                Console.ForegroundColor = value.Color;
                if (value.Value.Contains("\n")) {
                    string[] valueLines = value.Value.Split('\n');
                    for (var j = 0; j < valueLines.Length - 1; j++) {
                        Console.Write(valueLines[j]);
                        MoveToNextLineStart();
                    }

                    Console.Write(valueLines[valueLines.Length - 1]);
                    continue;
                }

                Console.Write(value.Value);
            }

            Console.ForegroundColor = ConsoleColor.White;

            // fill message box
            if (blames.Count == 0) {
                EditorHeader = null;
            }
            else {
                EditorHeader = blames[0].ToString();
            }
        }
    }
}