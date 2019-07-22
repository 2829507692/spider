import execjs
import os
#
# s = execjs.eval("""'red yellow blue'.length""")
# print(s)

ex = execjs.compile("""
function f(){
for(var i=0;i<5;i++){
console.log(i);
    }
}
""")
ex.call("f")//先编译后执行
print(execjs.get().name)
# os.environ["EXECJS_RUNTIME"] = "Node"
# print(execjs.get().name)

