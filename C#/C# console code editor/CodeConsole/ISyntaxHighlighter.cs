using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;

namespace CodeConsole {
    public interface ISyntaxHighlighter {
        List<ColoredValue> Highlight(
            List<string>        codeLines,
            ref Point           lastRenderEndPosition,
            out List<Exception> blames
        );

        List<ColoredValue> Highlight(string code);
    }

    [DebuggerDisplay("{" + nameof(debuggerDisplay) + ",nq}")]
    public class ColoredValue {
        public readonly ConsoleColor Color;

        public ColoredValue(string value, ConsoleColor color) {
            Value = value;
            Color = color;
        }

        public string Value { get; set; }

        [DebuggerBrowsable(DebuggerBrowsableState.Never)]
        private string debuggerDisplay =>
            $"{Color:G}: '{Value.Replace("\r", "\\r").Replace("\n", "\\n").Replace("\t", "\\t")}'";
    }
}