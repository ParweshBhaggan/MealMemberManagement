from User import Consultant, SuperAdmin, SystemAdmin

#consult = Consultant("Pawi", "Paw", "UserPawi", "PassPawi")


# consult = Consultant("Pawi", "Paw", "UserPawi", "PassPawi")
consult2 = Consultant("RodeCons", "Rode", "UserRode", "PassRode")
# consult.services.updatePassword("NewPassPawi")

sysadmin = SystemAdmin("SysPawi", "PawSys", "SystemPawi", "PassPawi")
#sysadmin2 = Consultant("RodeSys", "Rode", "UserRode", "PassRode")
sysadmin.services.updatePassword("NewSystemPassPawi")
sysadmin.services.addConsultant(consult2)

superAd = SuperAdmin()
print(superAd.username)
print(superAd.password)
superAd.services.addConsultant(consult2)