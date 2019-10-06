using System;

namespace CodeConsole.CodeEditor {
    public class CliEditorSettings {
        /// <summary>
        ///     Count of lines in editor is
        ///     limited to prevent performance hurting.
        /// </summary>
        internal const int MaxHighlightedLinesCount = 300;

        /// <summary>
        ///     Width of line number field at left side of code editor.
        /// </summary>
        public const int LineNumberWidth = 7; // " XXX | "

        internal const string       DefaultHeader = "No errors found.";
        internal const ConsoleColor FramesColor   = ConsoleColor.DarkGray;

        /// <summary>
        ///     Use only 1 editable line.
        /// </summary>
        public readonly bool SingleLineMode;

        /// <summary>
        ///     Use editor only for code highlighting.
        /// </summary>
        public readonly bool ReadOnly;

        /// <summary>
        ///     Highlight user input with specified <see cref="Highlighter" />.
        /// </summary>
        public bool SyntaxHighlighting => Highlighter != null;

        /// <summary>
        ///     Tab character in editor.
        /// </summary>
        public readonly string Tabulation;

        /// <summary>
        ///     User prompt used when editor
        ///     launched in single-line mode.
        /// </summary>
        public readonly string Prompt;

        /// <summary>
        ///     Current console highlighter.
        /// </summary>
        public readonly ISyntaxHighlighter Highlighter;

        /// <param name="singleLineMode">
        ///     Editor uses only 1 editable line.
        /// </param>
        /// <param name="readOnly"></param>
        /// <param name="prompt">
        ///     A permanent prompt to user to input something. Works only with
        ///     <paramref name="singleLineMode" />.
        /// </param>
        /// <param name="highlighter">
        ///     A code highlighter what is used in that editor.
        /// </param>
        public CliEditorSettings(
            bool               singleLineMode = false,
            bool               readOnly       = false,
            string             prompt         = null,
            ISyntaxHighlighter highlighter    = null
        ) {
            SingleLineMode = singleLineMode;
            Prompt = SingleLineMode
                ? prompt ?? ""
                : prompt != null
                    ? throw new ArgumentException()
                    : "";
            ReadOnly = readOnly;
            Tabulation  = new string(' ', 4);
            Highlighter = highlighter;
        }
    }
}