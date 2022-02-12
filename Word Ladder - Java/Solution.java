import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {

    // FASTER THAN 77% ON LEET CODE!!!!

    public static void main(String[] args) {
        System.out.println(
                ladderLength("ymain", "oecij", Arrays.asList("ymann", "yycrj", "oecij", "ymcnj", "yzcrj",
                        "yycij", "xecij", "yecij", "ymanj", "yzcnj", "ymain")));
    }

    public static int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> stringSet = new HashSet<>(wordList);
        if (!stringSet.contains(endWord))
            return 0;
        ArrayList<String> q = new ArrayList<String>();
        q.add(beginWord);
        int count = 0;
        while (!q.isEmpty()) {
            count++;
            for (int lSize = q.size(); lSize > 0; lSize--) {
                String cWord = q.get(0);
                q.remove(0);
                if (cWord.equals(endWord))
                    return count;
                for (int i = 0; i < cWord.length(); i++) {
                    char[] ch = cWord.toCharArray();
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == cWord.charAt(i))
                            continue;
                        ch[i] = c;
                        String testString = String.valueOf(ch);
                        if (stringSet.contains(testString)) {
                            q.add(testString);
                            stringSet.remove(testString);
                        }
                    }
                }
            }
            System.out.println(q);
        }
        System.out.println("Oof");
        return 0;
    }
}