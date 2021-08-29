#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            add_user: returns a user object
            and save the user to the database
        """

        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **keyword) -> User:
        """
        find user by a keyword arguments
        and return the first row found in users
        """
        valid_keyword = ["id", "email", "session_id", "reset_token"]
        keyword_keys = keyword.keys()
        if not all(
            keyword_keys in valid_keyword for keyword_keys in valid_keyword
                ):
            raise(InvalidRequestError)
        user = self._session.query(User).filter_by(**keyword).first()
        if user is None:
            raise(NoResultFound)
        else:
            return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
            update_user : will look up for the user
            using it's id, then update it's attributes
            based on the kwargs passed in the method arguments
            also commit changes to the database
        """
        valid_keyword = [
            "id",
            "email", "session_id", "reset_token", "hashed_password"]

        user = self.find_user_by(id=user_id)
        if user:
            for k, v in kwargs.items():
                if k in valid_keyword:
                    setattr(user, k, v)
                else:
                    # print(k in valid_keyword)
                    raise(ValueError)
            self._session.commit()
