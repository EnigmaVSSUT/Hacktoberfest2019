using System;
using System.Collections.Generic;

namespace CodeConsole.CodeEditor {
    /// <summary>
    ///     Embedded in console code editor with optional
    ///     syntax highlighting & handy keyboard shortcuts.
    /// </summary>
    public partial class CliEditor {
        private readonly CliEditorSettings settings;

        /// <summary>
        ///     Editor's code lines.
        /// </summary>
        private readonly List<string> lines = new List<string>();

        /// <summary>
        ///     Current editing line.
        ///     This property automatically calls
        ///     <see cref="RenderCode" /> when modified.
        ///     You should use <see cref="lines" />[<see cref="cursorY" />] when you
        ///     don't want to re-render input instead.
        /// </summary>
        private string Line {
            get => lines[cursorY];
            set {
                lines[cursorY] = value;
                // if line modified - it should be re-rendered
                RenderCode();
            }
        }

        /// <summary>
        ///     Creates new console editor instance.
        /// </summary>
        public CliEditor(
            CliEditorSettings editorSettings = null,
            string            firstCodeLine  = ""
        ) {
            settings = editorSettings ?? new CliEditorSettings();
            if (settings.SingleLineMode && settings.Prompt.Length > 0) {
                editBoxPoint.X = settings.Prompt.Length;
            }
            else {
                editBoxPoint.X = CliEditorSettings.LineNumberWidth;
            }

            lines.Add(firstCodeLine);
        }

        /// <summary>
        ///     Starts the editor (draws bounds, highlights code, etc.)
        ///     and returns prepared code lines when user finished editing.
        /// </summary>
        public string[] Run() {
            ConsoleUI.ClearLine();
            Console.Write(settings.Prompt);
            if (!settings.SingleLineMode) {
                DrawTopFrame();
            }

            editBoxPoint.Y = Console.CursorTop;
            cursorX        = Line.Length;

            // highlight first line
            lastRenderLinesCount = 1;
            RenderCode();

            return ReadLines();
        }

        /// <summary>
        ///     Reads and processes user input.
        /// </summary>
        private string[] ReadLines() {
            // writing loop
            var exit = false;
            while (!exit) {
                ConsoleKeyInfo key = Console.ReadKey(true);
                if (HandleViewAction(key)) {
                    continue;
                }

                newRenderStartPosition.Y = cursorY;
                newRenderStartPosition.X = cursorX;

                exit = HandleEditAction(key);
            }

            DrawBottomFrame();
            return lines.Count == 0
                ? new[] {
                    ""
                }
                : lines.ToArray();
        }

        /// <summary>
        ///     Occurs when lines count in editor exceeds maximal allowed value.
        /// </summary>
        private class FileTooLargeException : Exception {
            public FileTooLargeException() : base(
                "File too large to display. Please use external editor."
            ) { }
        }
    }
}