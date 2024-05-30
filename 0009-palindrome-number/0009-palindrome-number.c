bool isPalindrome(int x) {
    char s[256];
    sprintf(s,"%d",x);
    int length = strlen(s);
    for(int i=0; i<length; i++){
        if(s[i] != s[length-i-1]){
            return false;
        }
    }  
    return true;
}