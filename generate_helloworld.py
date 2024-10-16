# 定义要生成的 C++ 源码
cpp_source = """\
#include <iostream>
  
int main(int argc, char *argv[]) {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
"""

# 定义输出文件的名称
output_file = "helloworld.cpp"

# 将 C++ 源码写入文件
with open(output_file, "w") as file:
    file.write(cpp_source)

# 打印成功消息
print(f"Generated {output_file}")