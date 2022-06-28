# coding: utf-8


# 文件大小类
class FileSize():
    SIZE_UNIT = {
        "Byte": 1,
        "KB": 1024,
        "MB": 1048576,
        "GB": 1073741824,
        "TB": 1099511627776
    }

    def __init__(self, size):
        self._size = FileSize.Format(size)

    @staticmethod
    def Format(size):
        import re
        size_Byte = 0
        if isinstance(size, int):
            size_Byte = size
        elif isinstance(size, str):
            oSize = size.lstrip().upper().replace(" ", "")
            # 增加检查是否是全数字类型的字符串，添加默认的单位Byte
            if oSize.isdigit():
                size_Byte = int(oSize)
            pattern = re.compile(
                r"(\d*\.?(?=\d)\d*)(byte|kb|mb|gb|tb)", re.I)
            if match := pattern.match(oSize):
                m_size, m_unit = match.groups()
                m_size = int(m_size) if m_size.find(".") == -1 else float(m_size)
                size_Byte = m_size * FileSize.SIZE_UNIT[m_unit]
        return size_Byte

    # 返回字节为单位的值
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, newsize):
        self._size = FileSize(newsize)

    # 返回带单位的自动值
    @property
    def FriendValue(self):
        if self.size < FileSize.SIZE_UNIT["KB"]:
            unit = "Byte"
        elif self.size < FileSize.SIZE_UNIT["MB"]:
            unit = "KB"
        elif self.size < FileSize.SIZE_UNIT["GB"]:
            unit = "MB"
        elif self.size < FileSize.SIZE_UNIT["TB"]:
            unit = "GB"
        else:
            unit = "TB"
        print(unit)

        if (self.size % FileSize.SIZE_UNIT[unit]) == 0:
            return f"{self.size / FileSize.SIZE_UNIT[unit]}{unit}"
        else:
            return "%0.2f%s" % (
                round(float(self.size) / float(FileSize.SIZE_UNIT[unit]), 2), unit)

    def __str__(self):
        return self.FriendValue

    # 相加
    def __add__(self, other):
        if isinstance(other, FileSize):
            return FileSize(other.size + self.size)
        else:
            return FileSize(FileSize(other).size + self.size)

    def __sub__(self, other):
        if isinstance(other, FileSize):
            return FileSize(self.size - other.size)
        else:
            return FileSize(self.size - FileSize(other).size)

    def __gt__(self, other):
        return (
            isinstance(other, FileSize)
            and self.size > other.size
            or not isinstance(other, FileSize)
            and self.size > FileSize(other).size
        )

    def __lt__(self, other):
        return (
            isinstance(other, FileSize)
            and other.size > self.size
            or not isinstance(other, FileSize)
            and FileSize(other).size > self.size
        )

    def __ge__(self, other):
        return (
            isinstance(other, FileSize)
            and self.size >= other.size
            or not isinstance(other, FileSize)
            and self.size >= FileSize(other).size
        )

    def __le__(self, other):
        return (
            isinstance(other, FileSize)
            and other.size >= self.size
            or not isinstance(other, FileSize)
            and FileSize(other).size >= self.size
        )
