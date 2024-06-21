import bcrypt


class PasswordHasher:

    def hash_password(self, password):
        """哈希密码"""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def verify_password(self, password_attempt, hashed_password):
        """验证密码是否匹配存储的哈希密码"""
        if hashed_password is None:
            return False

        if bcrypt.checkpw(password_attempt.encode('utf-8'), hashed_password):
            return True
        else:
            return False


if __name__ == "__main__":
    hasher = PasswordHasher()
    hash_pwd = hasher.hash_password("mypassword123")
    print(hash_pwd)
    print("OK" if hasher.verify_password("mypassword123", hash_pwd) else "NO")
    print("OK" if hasher.verify_password("wrongpassword", hash_pwd) else "NO")
