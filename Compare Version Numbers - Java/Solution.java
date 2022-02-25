class Solution {
    public static void main(String[] args) {
        // String version1 = "1.001";
        // String version2 = "1.01";

        // String version1 = "1.0";
        // String version2 = "1.0.0";

        // String version1 = "0.1";
        // String version2 = "1.1";

        String version1 = "1.1";
        String version2 = "1.10";
        System.out.println(compareVersion(version1, version2));
    }

    public static int compareVersion(String version1, String version2) {
        int l1 = version1.length(), l2 = version2.length(), v1 = 0, v2 = 0, i1 = 0, i2 = 0;
        while (i1 < l1 || i2 < l2) {

            while (i1 < l1 && version1.charAt(i1) != '.') {
                v1 = 10 * v1 + (version1.charAt(i1) - '0');
                i1++;
            }

            while (i2 < l2 && version2.charAt(i2) != '.') {
                v2 = 10 * v2 + (version2.charAt(i2) - '0');
                i2++;
            }

            if (v1 > v2)
                return 1;
            else if (v1 < v2)
                return -1;
            else {
                v1 = 0;
                v2 = 0;
                i1++;
                i2++;
            }
        }

        return 0;

        // Brainstorm code
        /*
         * int ans = 0;
         * int v1 = 0;
         * int v1Prev = v1;
         * int v2 = 0;
         * int v2Prev = v2;
         * int v1Pointer = 0;
         * int v2Pointer = 0;
         * while (ans == 0 && (v1Pointer < version1.length() || v2Pointer <
         * version2.length())) {
         * while (v1 == v1Prev && v1Pointer < version1.length()) {
         * if (version1.charAt(v1Pointer) == '0') {
         * v1 *= 10;
         * v1Pointer++;
         * } else if (version1.charAt(v1Pointer) == '.') {
         * v1Pointer++;
         * break;
         * } else {
         * v1 = v1 * 10 + Character.getNumericValue(version1.charAt(v1Pointer));
         * v1Pointer++;
         * }
         * }
         * while (v2 == v2Prev && v2Pointer < version2.length()) {
         * if (version2.charAt(v2Pointer) == '0') {
         * v2 *= 10;
         * v2Pointer++;
         * } else if (version2.charAt(v2Pointer) == '.') {
         * v2Pointer++;
         * break;
         * } else {
         * v2 = v2 * 10 + Character.getNumericValue(version2.charAt(v2Pointer));
         * v2Pointer++;
         * }
         * }
         * if (v1 > v2)
         * return 1;
         * if (v2 > v1)
         * return -1;
         * if (version1.charAt(v1Pointer - 1) == '.' && version2.charAt(v2Pointer - 1)
         * == '.') {
         * v1 = 0;
         * v2 = 0;
         * }
         * v1Prev = v1;
         * v2Prev = v2;
         * }
         * return ans;
         */
    }
}