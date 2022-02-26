class Solution:
    def removeComments(self, source):
        def removeShort(code): # remove "//"
            if "//" in code:
                return code[:code.index("//")]
            else:
                return code

        largeComment = False
        sol = []
        for code in source:
            if largeComment == False: # not in large comment
                if "/*" in code and "//" not in code:
                    # start of the large comment
                    largeComment = True
                    stIndex = code.index("/*")
                    # print("1",code)
                    code = code[:stIndex]+code[stIndex+2:]
                    # print("2",code)
                    if "*/" in code:
                        # end of the large comment
                        largeComment = False
                        endIndex = code.index("*/")
                        # print("3",code)
                        code = code[:stIndex]+code[endIndex+2:]
                        # print("4",code)
                        if len(code):
                            sol.append(code)
                    else:
                        # still in the large comment
                        code = code[:stIndex]
                        temp = code
                elif "/*" in code and "//" in code:
                    if code.index("//") > code.index("/*"):
                        # start of the large comment
                        largeComment = True
                        stIndex = code.index("/*")
                        # print("1-2",code)
                        code = code[:stIndex]+code[stIndex+2:]
                        # print("2-2",code)
                        if "*/" in code:
                            # end of the large comment
                            largeComment = False
                            endIndex = code.index("*/")
                            # print("3-2",code)
                            code = code[:stIndex]+code[endIndex+2:]
                            # print("4-2",code)
                            if len(code):
                                sol.append(code)
                        else:
                            # still in the large comment
                            code = code[:stIndex]
                            temp = code
                    else:
                        code = removeShort(code)
                        if len(code):
                            sol.append(code)
                else: # no large comment
                    code = removeShort(code)
                    if len(code):
                        sol.append(code)
            else: # still in the large comment
                if "*/" in code:
                    # end the large comment
                    largeComment = False
                    endIndex = code.index("*/")
                    code = code[endIndex+2:]
                    temp += code
                    code = removeShort(code)
                    if len(temp):
                        sol.append(temp)
                else:
                    # still in the large comment
                    pass
        return sol


# main
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", 
"int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", 
"   testing */", "a = b + c;", "}"]
answer = ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
result = Solution.removeComments(0,source)
if not result == answer:
    print("Source:",source)
    print("Result:",result)
    print("Answer:",answer)
    print(result == answer)

source = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
answer = ["void func(int k) {","   k = k*2/4;","   k = k/2;*/","}"]
result = Solution.removeComments(0,source)
if not result == answer:
    print("Source:",source)
    print("Result:",result)
    print("Answer:",answer)
    print(result == answer)

source = ["main() {", "/* here is commments", "  // still comments */", "   double s = 33;", "   cout << s;", "}"]
answer = ["main() {","   double s = 33;","   cout << s;","}"]
result = Solution.removeComments(0,source)
if not result == answer:
    print("Source:",source)
    print("Result:",result)
    print("Answer:",answer)
    print(result == answer)

source = ["a//*b//*c","blank","d/*/e*//f"]
answer = ["a","blank","d/f"]
result = Solution.removeComments(0,source)
if not result == answer:
    print("Source:",source)
    print("Result:",result)
    print("Answer:",answer)
    print(result == answer)

source = ["a/*/b//*c","blank","d/*/e*//f"]
answer = ["ae*"]
result = Solution.removeComments(0,source)
if not result == answer:
    print("Source:",source)
    print("Result:",result)
    print("Answer:",answer)
    print(result == answer)
