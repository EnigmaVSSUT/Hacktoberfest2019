package codeforces;



static class IntIntPair implements Comparable<IntIntPair> {
	public final int first;
	public final int second;

	public static IntIntPair makePair(int first, int second) {
		return new IntIntPair(first, second);
	}

	public IntIntPair(int first, int second) {
		this.first = first;
		this.second = second;
	}

	public boolean equals(Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}

		IntIntPair pair = (IntIntPair) o;

		return first == pair.first && second == pair.second;
	}

	public int hashCode() {
		int result = first;
		result = 31 * result + second;
		return result;
	}

	public String toString() {
		return "(" + first + "," + second + ")";
	}

	public int compareTo(IntIntPair o) {
		int value = Integer.compare(first, o.first);
		if (value != 0) {
			return value;
		}
		return Integer.compare(second, o.second);
	}

}
