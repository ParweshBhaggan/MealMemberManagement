from UserServices import UserServices


class SuperAdmin:
    services = UserServices()
    username = 'superadmin'#'super_admin'
    password = 'admin123'#'Admin_123?'

# superadmin = SuperAdmin()

# #print(superadmin.username, superadmin.password)

# superadmin.services.updatePassword(superadmin,'newpassword')

# admin = SystemAdmin('Rode','Wilson', 'admin', 'adminpassword')
# admin1 = SystemAdmin('Roderick','Wil', 'admin1', 'adminpassword')
# admin2 = SystemAdmin('Roder','Wils', 'admin2', 'adminpassword')

# superadmin.services.addAdmin(admin)
# superadmin.services.addAdmin(admin1)
# superadmin.services.addAdmin(admin2)

# superadmin.services.checkUsers()

# superadmin.services.deleteAdmin(admin1)

# superadmin.services.resetAdminPassword('newpassword', admin2)

# admin3 = SystemAdmin('Test3','Admin3', 'admin', 'password')
# superadmin.services.updateAdmin(admin3)

# consultant = Consultant('Test','Consultant', 'consultant', 'password')
# consultant1 = Consultant('Test1','Consultant', 'consultant1', 'password')
# consultant2 = Consultant('Test2','Consultant', 'consultant2', 'password')

# superadmin.services.addConsultant(consultant)
# superadmin.services.addConsultant(consultant1)
# superadmin.services.addConsultant(consultant2)

# superadmin.services.checkUsers()

# superadmin.services.deleteConsultant(consultant1)

# superadmin.services.resetConsultantPassword('newpassword', consultant2)

# consultant3 = Consultant('Test3','Consultant3', 'consultant', 'password')
# superadmin.services.updateConsultant(consultant3)

# member = Member('Roderick','Wilson', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username', 'password')
# member1 = Member('Test1','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username1', 'password')
# member2 = Member('Test2','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username2', 'password')

# superadmin.services.addMember(member)
# superadmin.services.addMember(member1)
# superadmin.services.addMember(member2)

# superadmin.services.checkUsers()

# superadmin.services.deleteMember(member1)

# superadmin.services.resetMemberPassword('newpassword', member2)

# member3 = Member('Test3','Member3', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email3@hotmail.com', +31633333333, 'username2', 'password')
# superadmin.services.updateMember(member3)

# superadmin.services.searchMember('username2')

# logViewer()
