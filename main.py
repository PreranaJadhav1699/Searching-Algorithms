import time
from flask import Flask, render_template, request

app = Flask(__name__)

#-----------------Search Algorithms-----------------#


# Linear Search
# Goes through the list of numbers one by one and compares each element with the target.

def linearSearch(arr, target):
    start = time.time()
    found = []
    for i in range(len(arr)):
        if arr[i] == target:
            found.append(i)
    return {
        "found": len(found) > 0,
        "indices": found,
        "time": time.time() - start
    }

# Binary Search in Sorted Array
# Works only on a sorted array.Starts from the middle element,checks if it is equal to the target, and based on that moves either to the left side or the right side part of the array.

def binarySearch(arr, target):
    start = time.time()
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return {
                "found": True,
                "index": mid,
                "time": time.time() - start
            }
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return {
        "found": False,
        "index": -1,
        "time": time.time() - start
    }

# Binary Search Tree 
# First builds a BST from the given array then searches for the target in the tree. At each node compares the value with the target and moves to the left child if the target is smaller or to the right child if the target is large.Returns whether the target exists in the BST.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insertNode(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insertNode(root.left, val)
    elif val > root.val:
        root.right = insertNode(root.right, val)
    return root


def makeBst(arr):
    if not arr:
        return None
    root = Node(arr[0])
    for x in arr[1:]:
        root = insertNode(root, x)
    return root


def findInBst(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    elif root.val > target:
        return findInBst(root.left, target)
    else:
        return findInBst(root.right, target)


def searchBst(arr, target):
    start = time.time()
    root = makeBst(arr)
    found = findInBst(root, target)
    return {
        "found": found,
        "time": time.time() - start
    }

# Red-Black Tree
# Uses a self-balancing binary search tree where each node is marked as red or black. The extra color rules and rotations keep the tree roughly balanced after insertions,
# so the height stays close to log n. The search then works like a normal BST:
# move left if the target is smaller, right if it is larger, and report if it is found.

class RBNode:
    def __init__(self, key, color="R"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(0, "B")
        self.root = self.nil

    def search(self, node, key):
        if node == self.nil or key == node.key:
            return node != self.nil
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fixInsert(self, z):
        while z.parent and z.parent.color == "R":
            if z.parent == z.parent.parent.right:
                u = z.parent.parent.left
                if u.color == "R":
                    u.color = "B"
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotateRight(z)
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self.rotateLeft(z.parent.parent)
            else:
                u = z.parent.parent.right
                if u.color == "R":
                    u.color = "B"
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotateLeft(z)
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self.rotateRight(z.parent.parent)

            if z == self.root:
                break

        self.root.color = "B"

    def insert(self, key):
        z = RBNode(key)
        z.left = self.nil
        z.right = self.nil
        y = None
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        if z.parent is None:
            z.color = "B"
            return
        if z.parent.parent is None:
            return
        self.fixInsert(z)


def searchRbt(arr, target):
    start = time.time()
    rbt = RBTree()
    for x in arr:
        rbt.insert(x)
    found = rbt.search(rbt.root, target)
    return {
        "found": found,
        "time": time.time() - start
    }


def getPerfData(arr, target):
    sizes = []
    lin = []
    binArr = []
    bstArr = []
    rbtArr = []

    n = len(arr)
    testSizes = [
        n // 4 if n >= 4 else n,
        n // 2 if n >= 2 else n,
        n,
        n * 2,
        n * 4
    ]
    testSizes = [max(1, s) for s in testSizes]

    for s in testSizes:
        if s > 100000:
            continue
        sizes.append(s)

        testArr = (arr * (s // n + 1))[:s] if n > 0 else []
        if not testArr:
            testArr = [1] * s

        t = target if target in testArr else testArr[len(testArr) // 2] if testArr else 1

        r = linearSearch(testArr, t)
        lin.append(r["time"])

        sortedTest = sorted(testArr)
        r = binarySearch(sortedTest, t)
        binArr.append(r["time"])

        r = searchBst(testArr, t)
        bstArr.append(r["time"])

        r = searchRbt(testArr, t)
        rbtArr.append(r["time"])

    return {
        "sizes": sizes,
        "linear": lin,
        "binary": binArr,
        "bst": bstArr,
        "rbt": rbtArr
    }

# -----------------FLASK----------------- #

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    compare = None
    perfData = None
    allCompare = None

    numbers = ""
    target = None
    method = "linear"

    if request.method == "POST":
        numbers = request.form["numbers"]
        target = int(request.form["target"])
        method = request.form["method"]

        # allow spaces / extra commas
        nums = [int(x.strip()) for x in numbers.split(",") if x.strip() != ""]

        if method == "linear":
            res = linearSearch(nums, target)
            result = f"Found at index {res['indices']}" if res["found"] else "Not found"
            compare = res

        elif method == "binary":
            sortedNums = sorted(nums)
            res = binarySearch(sortedNums, target)
            result = f"Found at index {res['index']}" if res["found"] else "Not found"
            compare = res

        elif method == "bst":
            res = searchBst(nums, target)
            result = "Found" if res["found"] else "Not found"
            compare = res

        elif method == "rbt":
            res = searchRbt(nums, target)
            result = "Found" if res["found"] else "Not found"
            compare = res

        allCompare = {
            "Linear Search": linearSearch(nums, target),
            "Binary Search": binarySearch(sorted(nums), target),
            "Binary Search Tree": searchBst(nums, target),
            "Red Black Tree": searchRbt(nums, target)
        }

        perfData = getPerfData(nums, target)

    return render_template(
        "home.html",
        result=result,
        compare=compare,
        all_compare=allCompare,
        perf_data=perfData,
        numbers=numbers,
        target=target,
        method=method
    )

if __name__ == "__main__":
    app.run(debug=True)
