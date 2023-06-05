from collections import OrderedDict
from bing_image_downloader import downloader
import os
from concurrent.futures import ThreadPoolExecutor

def download_image(keyword, search_term, path, num_images=1):
    # Create a subdirectory for each keyword
    sub_path = os.path.join(path, keyword)
    if not os.path.exists(sub_path):
        os.makedirs(sub_path)
    # Download the image with the search_term as the search keyword
    downloader.download(search_term, limit=num_images, output_dir=sub_path, adult_filter_off=True, force_replace=False, timeout=60)

def download_images(keyword_dict, path, num_images=1):
    # Check if the path exists, if not, create it.
    if not os.path.exists(path):
        os.makedirs(path)

    with ThreadPoolExecutor() as executor:
        for key, values in keyword_dict.items():
            for value in values:
                executor.submit(download_image, key, value, path, num_images)
    print('Download Complete')



# keyWordDict = OrderedDict({
#     "开放世界": ["Python解释型语言, 强大社区和库支持", "Python is an interpreted language, with a strong community and library support"],
#     "次时代": ["Python 3.9或者更新的版本", "Python 3.9 or newer versions"],
#     "专武（专一武器）": ["Python的IPython环境，以及强大的数据科学库，例如pandas和numpy", "Python's IPython environment and powerful data science libraries, such as pandas and numpy"],
#     "圣遗物": ["Python的内置函数和标准库", "Python's built-in functions and standard library"],
#     "二次元": ["使用matplotlib库创建的二维图形", "Creating 2D graphics using matplotlib library"],
#     "每日委托": ["LeetCode或者其他在线OJ的Python挑战题目", "Python challenge questions on LeetCode or other online OJs"],
#     "元素反应": ["Python的语法糖，例如列表推导式，生成器表达式，装饰器等", "Python's syntactic sugar, such as list comprehension, generator expressions, decorators, etc."],
#     "抽卡": ["在编写Python程序时出现的不同类型的错误，例如SyntaxError, TypeError, ValueError等", "Different types of errors that occur when writing Python programs, such as SyntaxError, TypeError, ValueError, etc."],
#     "联机": ["在GitHub上合作完成Python项目", "Collaborating on Python projects on GitHub"],
#     "跑图": ["使用networkx库解决图论问题", "Solving graph theory problems using networkx library"],
#     "冒险RPG": ["使用Pygame库制作的RPG游戏", "Making RPG games using Pygame library"],
#     "传送锚点": ["Python的循环控制结构，如for或while", "Python's loop control structures, such as for or while"],
#     "盘子可以偷": ["Python的垃圾回收机制无法处理的循环引用问题", "Cyclic reference problems that Python's garbage collection mechanism cannot handle"],
#     "前面的区域， 以后再来探索吧": ["Python的GIL（全局解释锁）问题", "Python's GIL (Global Interpreter Lock) issue"],
#     "抽象解谜": ["在Python中解决递归或者动态规划问题", "Solving recursion or dynamic programming problems in Python"],
#     "剧情不能跳过": ["Python的PEP8编码规范，不能跳过的错误处理，例如try/except结构", "Python's PEP8 coding style guide, error handling that cannot be skipped, such as try/except structure"],
#     "蹦蹦炸弹": ["在Python中解决复杂的问题，例如并发或多线程问题", "Solving complex problems in Python, such as concurrency or multithreading issues"],
#     "3D体验": ["使用NumPy和Matplotlib创建3D图形或动画", "Creating 3D graphics or animations using NumPy and Matplotlib"],
# })
keyWordDict = {
    "开放世界": ["全球化的机械设计与制造，例如全球供应链中的机械零部件制造",
                 "Global mechanical design and manufacturing, such as mechanical parts manufacturing in global supply chains"],
    "次时代": ["新兴的机械工程技术和趋势，例如3D打印和自动化生产",
               "Emerging mechanical engineering technologies and trends, such as 3D printing and automated production"],
    "专武（专一武器）": ["专业的机械设备和技术，例如数控机床和机器人",
                      "Professional mechanical devices and techniques, such as CNC machines and robots"],
    "圣遗物": ["机械工程的基本理论，例如热力学和固体力学",
              "Fundamental theories in mechanical engineering, such as thermodynamics and solid mechanics"],
    "二次元": ["二阶动力系统的建模和分析，例如振动分析和控制",
               "Modeling and analysis of second-order dynamic systems, such as vibration analysis and control"],
    "每日委托": ["日常的机械设计和维护工作，例如CAD设计和设备故障排查",
                "Daily mechanical design and maintenance work, such as CAD design and equipment troubleshooting"],
    "元素反应": ["机械系统中的互相作用，例如齿轮间的动力传递",
                 "Interactions in mechanical systems, such as power transmission between gears"],
    "抽卡": ["机械设计的可能结果，可能出现的结果有成功、失败、需要优化等",
             "Possible outcomes of mechanical designs, possible outcomes include success, failure, need for optimization, etc."],
    "联机": ["团队合作进行机械项目，例如一组工程师共同完成一个机器人设计",
             "Team collaboration for mechanical projects, such as a group of engineers jointly completing a robot design"],
    "跑图": ["机械图纸的制作和解析，例如使用AutoCAD制作零件图",
             "Making and interpreting mechanical drawings, such as using AutoCAD to create part drawings"],
    "冒险RPG": ["探索新的设计方案和制造工艺，例如开发新的动力系统或改进制造流程",
                "Exploring new design schemes and manufacturing processes, such as developing new power systems or improving manufacturing workflows"],
    "传送锚点": ["机械设计的迭代和优化，例如根据测试结果优化产品设计",
                "Iteration and optimization of mechanical design, for example, optimizing product design based on test results"],
    "盘子可以偷": ["机械故障和设计失误，例如设计不合理可能导致设备过早磨损",
                   "Mechanical failures and design errors, such as unreasonable design could lead to premature equipment wear"],
    "前面的区域，以后再来探索吧": ["未开发的机械工程领域，例如微纳机电系统和柔性机械",
                                "Undeveloped areas in mechanical engineering, such as micro-nano electromechanical systems and soft robotics"],
    "抽象解谜": ["解决复杂的机械问题，例如多物理场耦合问题的解决",
                "Solving complex mechanical problems, such as solving multiphysics coupling problems"],
    "剧情不能跳过": ["遵守工程规则和安全标准，例如遵守ISO标准和工作场所的安全规定",
                    "Following engineering rules and safety standards, such as adhering to ISO standards and safety regulations in the workplace"],
    "蹦蹦炸弹": ["机械故障和意外事件，例如设备故障或工作场所事故",
                "Mechanical failures and accidents, such as equipment breakdowns or workplace accidents"],
    "3D体验": ["三维机械设计和建模，例如使用SolidWorks进行产品设计",
               "Three-dimensional mechanical design and modeling, such as using SolidWorks for product design"]
}

#  "开放世界": ["高校的自由学术环境", "The free academic environment of universities"],
# 模仿第一个键值对， 给后面的也加上英文解释
topic = "ME"

if __name__ == "__main__":
    download_images(keyWordDict, f'./{topic}/images', 10)

