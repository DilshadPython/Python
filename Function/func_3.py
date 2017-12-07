def profile(fname, lname, address, postcode, city):
    print('Your full details is below:\n %s \n %s \n %s \n %s \n %s' % (fname,
                                                                        lname,
                                                                        address,
                                                                        postcode,
                                                                        city))

profile('Dilshad', 'Abdulla', '6 Ursula Gould Way', 'E14 7FX', 'London')

profile('Shvan', 'Abdulla', '301 Hallmark Court', 'E16 5TT', 'London')


print('***'*25)
def myprofile(fname, lname, address, postcode, city):
    print('Your full details is below:\n First name: {} \n Last name{} \n Address: {} \
                                        \n Post code: {} \n City: {}'.format(fname,
                                                                            lname,
                                                                            address,
                                                                            postcode,
                                                                            city))

myprofile('Susane', 'Paul', '14 London Roadt', 'P17 11F', 'Porthsmouth')