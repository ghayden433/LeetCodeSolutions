int lengthOfLastWord(char* s) {
    char* pointer = s + strlen(s) - 1;
    while (*pointer == ' ') pointer--;
    char *wordEnd = pointer;
    while (pointer >= s && *pointer != ' ') pointer--;
    return wordEnd - pointer;

    return 0;
}