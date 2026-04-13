class Solution {
    public int evalRPN(String[] tokens) {
        List<Integer> stack = new ArrayList<>();

        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i].equals("+")) {
                stack.add(stack.remove(stack.size() - 1) + stack.remove(stack.size() - 1));
            } else if (tokens[i].equals("-")) {
                int second = stack.remove(stack.size() - 1);
                int first = stack.remove(stack.size() - 1);
                stack.add(first - second);
            } else if (tokens[i].equals("*")) {
                stack.add(stack.remove(stack.size() - 1) * stack.remove(stack.size() - 1));
            } else if (tokens[i].equals("/")) {
                int second = stack.remove(stack.size() - 1);
                int first = stack.remove(stack.size() - 1);
                stack.add(first / second);
            } else {
                stack.add(Integer.parseInt(tokens[i]));
            }
        }
        return stack.get(0);
    }
}