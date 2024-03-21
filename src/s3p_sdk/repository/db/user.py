from s3p_sdk.types import S3PUser, S3PRole
from .main import ps_connection


class Users:
    """
    Analytics schema of S3P DB class
    """
    schema: str = 'users'

    @classmethod
    def auth(cls, telegram_id: int) -> S3PUser:
        """
        Метод для авторизации пользователя в S3P
        """
        assert isinstance(telegram_id, int)
        with ps_connection() as connection:
            with connection.cursor() as cursor:
                cursor.callproc(f'{Users.schema}.auth', (telegram_id, None))
                output = cursor.fetchall()

                roles: list[S3PRole] = [S3PRole(row[3], row[4], None) for row in output]
                if output and len(output) > 0:
                    return S3PUser(
                        output[0][0],
                        output[0][1],
                        output[0][2],
                        tuple(roles)
                    )
                else:
                    raise UserWarning(f'No users found for telegram id: {telegram_id}')

    @classmethod
    def roles(cls, user_id: int, src_id: int = None) -> tuple[tuple[int, str]]:
        """
        Список ролей, доступные для пользователя.
        Если указан src_id, то будет выведен список ролей, доступных для этого источника и пользователя.
        Если src_id не указан, но будет выведен список всех ролей, доступных для пользователя
        :param user_id:
        :param src_id:
        :return:
        """
        with ps_connection() as connection:
            with connection.cursor() as cursor:
                if src_id:
                    params = (user_id, src_id)
                else:
                    params = (user_id, )

                cursor.callproc(f'{Users.schema}.roles', params)
                output = cursor.fetchall()
                return output
