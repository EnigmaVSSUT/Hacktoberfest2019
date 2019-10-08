package codeforces;

/**
 * @author johnny16
 *
 */
public class UF {

	private int count; // num of components
	private int id[]; // id[i] = root of i
	private int rank[]; // rank[i] = size of subtree rooted at i (cant be more than 31)

	UF(int n) {
		count = n;
		id = new int[n];
		rank = new int[n];
		int i;
		for (i = 0; i < n; i++) {
			id[i] = i;			// each tree is its own root
			rank[i] = 0;
		}
	}

	/**
	 * 
	 * @param p
	 * @return the root of the parameter p
	 */
	int root(int p) {
		while (p != id[p]) {
			id[p] = id[id[p]]; // path compression
			p = id[p];
		}
		return p;
	}
/**
 * 
 * @param a
 * @param b
 * @return true if a and b belong to same subtree
 */
	boolean find(int a, int b) {
		if (root(a) == root(b))
			return true;
		return false;
	}
/**
 * union of subtree a with b according to rank
 * @param a
 * @param b
 */
	void union(int a, int b) {
		int root_a = root(a);
		int root_b = root(b);
		if (root_a == root_b)
			return;
		if (rank[root_a] > rank[root_b])
			id[root_b] = root_a;
		else if (rank[root_b] > rank[root_a])
			id[root_a] = root_b;
		else {
			id[root_a] = root_b;
			rank[root_b]++;
		}
		count--;
	}
/**
 * 
 * @return number of components in tree
 */
	int numOfComponents() {
		return count;
	}
}
