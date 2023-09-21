#The program should then print out the names of friends who have not RSVP'd, 
#the names of friends who were not invited but RSVP'd, and the names of friends who are common in both lists (i.e., invited and RSVP'd).


friendsInvited = ['James', 'Jones', 'Anna', 'Bettany', 'Kenneth', 'Olivia']
friendsRSVP = ['Jones', 'Hanna', 'Lianne', 'Bettany', 'Lars', 'Peter', 'Benjamin', 'Olivia']

def checkWhoRSVP(invited, RSVP):
    didRSVP = []
    noRSVP = []
    RSVPbutNoInv = []
    for friend in invited:
        for otherFriend in RSVP:
            if friend == otherFriend:
                didRSVP.append(friend)

    for friend in invited:
        if didRSVP.count(friend) == 0:
            noRSVP.append(friend)

    for friend in friendsRSVP:
         if didRSVP.count(friend) == 0:
            RSVPbutNoInv.append(friend)

    print('invited and RSVPed:')
    print(didRSVP)
    print('\n')

    print('invited but did not RSVP:')
    print(noRSVP)
    print('\n')

    print('Not invited but RSVPed:')
    print(RSVPbutNoInv)
    print('\n')

checkWhoRSVP(friendsInvited, friendsRSVP)
