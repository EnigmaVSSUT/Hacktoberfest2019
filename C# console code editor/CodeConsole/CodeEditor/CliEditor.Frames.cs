using System;
using static CodeConsole.ConsoleUI;

namespace CodeConsole.CodeEditor {
    public partial class CliEditor {
        private void DrawTopFrame() {
            Console.WriteLine("Press [Esc] twice to exit code editor");
            if (settings.SyntaxHighlighting) {
                // draw header frame
                Write(
                    ("┌─────" + new string('─', Console.BufferWidth - editBoxPoint.X) + "\n" + "| ",
                     CliEditorSettings.FramesColor)
                );
                // mark position of header
                headerPoint.X = Console.CursorLeft;
                headerPoint.Y = Console.CursorTop;
                // draw editor frame
                WriteLine(
                    (CliEditorSettings.DefaultHeader + "\n" +
                    "└────┬" + new string('─', Console.BufferWidth - editBoxPoint.X),
                     CliEditorSettings.FramesColor)
                );
            }
            else {
                // else draw upper bound
                WriteLine(
                    ("─────┬" + new string('─', Console.BufferWidth - editBoxPoint.X),
                     CliEditorSettings.FramesColor)
                );
            }
        }

        private void DrawBottomFrame() {
            if (settings.SingleLineMode) {
                return;
            }

            // move to editor lower bound and
            // render bottom frame
            cursorY            = lines.Count;
            Console.CursorLeft = 0;
            WriteLine(
                ("─────┴" + new string('─', Console.BufferWidth - editBoxPoint.X),
                 CliEditorSettings.FramesColor)
            );
        }

        /// <summary>
        ///     In multiline mode, prints line
        ///     number on left side of editor.
        ///     That number not included in code.
        /// </summary>
        private void DrawCurrentLineNumber() {
            DrawLineNumber(cursorY + 1);

            if (settings.SyntaxHighlighting && lines.Count > CliEditorSettings.MaxHighlightedLinesCount) {
                throw new FileTooLargeException();
            }
        }

        /// <summary>
        ///     Prints specified line number
        ///     on left side of console.
        /// </summary>
        public static void DrawLineNumber(int lineNumber) {
            var view = "";

            // left align line number
            //    X |
            if (lineNumber < 10) {
                view += "   ";
            }
            //   XX |
            else if (lineNumber < 100) {
                view += "  ";
            }
            //  XXX |
            else {
                view += " ";
            }

            // append line number and right aligner
            view += lineNumber + " | ";
            Write((view, CliEditorSettings.FramesColor));
        }
    }
}