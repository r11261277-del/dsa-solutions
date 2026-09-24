class SegmentTree {

    private static final int MAXK = 6;
    private int k;
    private int n;
    private int[][] tree;

    public SegmentTree(int[] nums, int k) {
        this.k = k;
        this.n = nums.length;
        int size = 2 << Integer.toBinaryString(n).length();
        tree = new int[size][MAXK];
        build(nums, 1, 0, n - 1);
    }

    private void makeLeaf(int o, int value) {
        Arrays.fill(tree[o], 0);
        int r = value % k;
        tree[o][r] = 1;
        tree[o][k] = r;
    }

    private void mergePre(int[] left, int[] right, int[] result) {
        int mulL = left[k];
