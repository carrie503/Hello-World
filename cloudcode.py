#testing
@skygear.op("update-writer", user_required=True)
def update_writer(detail):
    with _get_engine().begin() as conn:
        trans = conn.begin()
        try:
            update_skygear_user_email(conn, detail['recordId'], detail['email'])
            conn.execute(sa.text('''
                UPDATE "{schema}"."TaylorsUser"
                SET "email" = :email,
                    "name" = :name,
                    "address" = :address,
                    "postalCode" = :postalCode,
                    "city" = :city,
                    "country" = :country,
                    "contactNo" = :contactNo
                WHERE _id = :id
                '''.format(
                    schema=db_schema,
                )),
                id=detail['recordId'],
                email=detail['email'],
                name=detail['name'],
                address=detail['address'],
                postalCode=detail['postalCode'],
                city=detail['city'],
                country=detail['country'],
                contactNo=detail['contactNo']
            )
            trans.commit()
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
            trans.rollback()
            if e.__class__.__name__ == 'IntegrityError' and e.orig.pgcode == '23505':
                raise Exception('An account already exists with this email address.')
            else:
                raise Exception(sys.exc_info()[0])

@skygear.op("update-test", user_required=True)
def update_writer(detail):
    with _get_engine().begin() as conn:
        trans = conn.begin()
        try:
            update_skygear_user_email(conn, detail['recordId'], detail['email'])
            conn.execute(sa.text('''
                UPDATE "{schema}"."TaylorsUser"
                SET "email" = :email,
                    "name" = :name,
                    "address" = :address,
                    "postalCode" = :postalCode,
                    "city" = :city,
                    "country" = :country,
                    "contactNo" = :contactNo
                WHERE _id = :id
                '''.format(
                    schema=db_schema,
                )),
                id=detail['recordId'],
                email=detail['email'],
                name=detail['name'],
                address=detail['address'],
                postalCode=detail['postalCode'],
                city=detail['city'],
                country=detail['country'],
                contactNo=detail['contactNo']
            )
            trans.commit()
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
            trans.rollback()
            if e.__class__.__name__ == 'IntegrityError' and e.orig.pgcode == '23505':
                raise Exception('An account already exists with this email address.')
            else:
                raise Exception(sys.exc_info()[0])

@skygear.op("test-test", user_required=True)
def update_writer(detail):
    with _get_engine().begin() as conn:
        trans = conn.begin()
        try:
            update_skygear_user_email(conn, detail['recordId'], detail['email'])
            conn.execute(sa.text('''
                UPDATE "{schema}"."TaylorsUser"
                SET "email" = :email,
                    "name" = :name,
                    "address" = :address,
                    "postalCode" = :postalCode,
                    "city" = :city,
                    "country" = :country,
                    "contactNo" = :contactNo
                WHERE _id = :id
                '''.format(
                    schema=db_schema,
                )),
                id=detail['recordId'],
                email=detail['email'],
                name=detail['name'],
                address=detail['address'],
                postalCode=detail['postalCode'],
                city=detail['city'],
                country=detail['country'],
                contactNo=detail['contactNo']
            )
            trans.commit()
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
            trans.rollback()
            if e.__class__.__name__ == 'IntegrityError' and e.orig.pgcode == '23505':
                raise Exception('An account already exists with this email address.')
            else:

@skygear.op("test-run", user_required=True)
def update_writer(detail):
    with _get_engine().begin() as conn:
        trans = conn.begin()
        try:
            update_skygear_user_email(conn, detail['recordId'], detail['email'])
            conn.execute(sa.text('''
                UPDATE "{schema}"."TaylorsUser"
                SET "email" = :email,
                    "name" = :name,
                    "address" = :address,
                    "postalCode" = :postalCode,
                    "city" = :city,
                    "country" = :country,
                    "contactNo" = :contactNo
                WHERE _id = :id
                '''.format(
                    schema=db_schema,
                )),
                id=detail['recordId'],
                email=detail['email'],
                name=detail['name'],
                address=detail['address'],
                postalCode=detail['postalCode'],
                city=detail['city'],
                country=detail['country'],
                contactNo=detail['contactNo']
            )
            trans.commit()
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
            trans.rollback()
            if e.__class__.__name__ == 'IntegrityError' and e.orig.pgcode == '23505':
                raise Exception('An account already exists with this email address.')
            else:

@skygear.op("test-run-test", user_required=True)
def update_writer(detail):
    with _get_engine().begin() as conn:
        trans = conn.begin()
        try:
            update_skygear_user_email(conn, detail['recordId'], detail['email'])
            conn.execute(sa.text('''
                UPDATE "{schema}"."TaylorsUser"
                SET "email" = :email,
                    "name" = :name,
                    "address" = :address,
                    "postalCode" = :postalCode,
                    "city" = :city,
                    "country" = :country,
                    "contactNo" = :contactNo
                WHERE _id = :id
                '''.format(
                    schema=db_schema,
                )),
                id=detail['recordId'],
                email=detail['email'],
                name=detail['name'],
                address=detail['address'],
                postalCode=detail['postalCode'],
                city=detail['city'],
                country=detail['country'],
                contactNo=detail['contactNo']
            )
            trans.commit()
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
            trans.rollback()
            if e.__class__.__name__ == 'IntegrityError' and e.orig.pgcode == '23505':
                raise Exception('An account already exists with this email address.')
            else:
