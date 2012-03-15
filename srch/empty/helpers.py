import string
import logging

def cleanup_term(term):
    """in: a term from a document
    out: a canonical form of that term, or None if there's no usable term"""
    original_term = term
    
    term = term.translate(None, string.punctuation)
    
    if term == '':
        return None
        
    if term.isalnum():
        return term.lower()
        
    raise ValueError("cannot canonicalize term: " + original_term)

def load_document(docname):
    """in: the name of a document
    out: the contents of the document as a string"""
    
    if docname == "us_constitution":
        #return "We the people of the United States of America"
        return """We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.

Article. I.

Section. 1.

All legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives.

Section. 2.

The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the Qualifications requisite for Electors of the most numerous Branch of the State Legislature.

No Person shall be a Representative who shall not have attained to the Age of twenty five Years, and been seven Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State in which he shall be chosen.

Representatives and direct Taxes shall be apportioned among the several States which may be included within this Union, according to their respective Numbers, which shall be determined by adding to the whole Number of free Persons, including those bound to Service for a Term of Years, and excluding Indians not taxed, three fifths of all other Persons. The actual Enumeration shall be made within three Years after the first Meeting of the Congress of the United States, and within every subsequent Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until such enumeration shall be made, the State of New Hampshire shall be entitled to chuse three, Massachusetts eight, Rhode-Island and Providence Plantations one, Connecticut five, New-York six, New Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South Carolina five, and Georgia three.

When vacancies happen in the Representation from any State, the Executive Authority thereof shall issue Writs of Election to fill such Vacancies.

The House of Representatives shall chuse their Speaker and other Officers; and shall have the sole Power of Impeachment.

Section. 3.

The Senate of the United States shall be composed of two Senators from each State, chosen by the Legislature thereof for six Years; and each Senator shall have one Vote.

Immediately after they shall be assembled in Consequence of the first Election, they shall be divided as equally as may be into three Classes. The Seats of the Senators of the first Class shall be vacated at the Expiration of the second Year, of the second Class at the Expiration of the fourth Year, and of the third Class at the Expiration of the sixth Year, so that one third may be chosen every second Year; and if Vacancies happen by Resignation, or otherwise, during the Recess of the Legislature of any State, the Executive thereof may make temporary Appointments until the next Meeting of the Legislature, which shall then fill such Vacancies.

No Person shall be a Senator who shall not have attained to the Age of thirty Years, and been nine Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State for which he shall be chosen.

The Vice President of the United States shall be President of the Senate, but shall have no Vote, unless they be equally divided.

The Senate shall chuse their other Officers, and also a President pro tempore, in the Absence of the Vice President, or when he shall exercise the Office of President of the United States.

The Senate shall have the sole Power to try all Impeachments. When sitting for that Purpose, they shall be on Oath or Affirmation. When the President of the United States is tried, the Chief Justice shall preside: And no Person shall be convicted without the Concurrence of two thirds of the Members present.

Judgment in Cases of Impeachment shall not extend further than to removal from Office, and disqualification to hold and enjoy any Office of honor, Trust or Profit under the United States: but the Party convicted shall nevertheless be liable and subject to Indictment, Trial, Judgment and Punishment, according to Law.

Section. 4.

The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such Regulations, except as to the Places of chusing Senators.

The Congress shall assemble at least once in every Year, and such Meeting shall be on the first Monday in December, unless they shall by Law appoint a different Day.

Section. 5.

Each House shall be the Judge of the Elections, Returns and Qualifications of its own Members, and a Majority of each shall constitute a Quorum to do Business; but a smaller Number may adjourn from day to day, and may be authorized to compel the Attendance of absent Members, in such Manner, and under such Penalties as each House may provide.

Each House may determine the Rules of its Proceedings, punish its Members for disorderly Behaviour, and, with the Concurrence of two thirds, expel a Member.

Each House shall keep a Journal of its Proceedings, and from time to time publish the same, excepting such Parts as may in their Judgment require Secrecy; and the Yeas and Nays of the Members of either House on any question shall, at the Desire of one fifth of those Present, be entered on the Journal.

Neither House, during the Session of Congress, shall, without the Consent of the other, adjourn for more than three days, nor to any other Place than that in which the two Houses shall be sitting.

Section. 6.

The Senators and Representatives shall receive a Compensation for their Services, to be ascertained by Law, and paid out of the Treasury of the United States. They shall in all Cases, except Treason, Felony and Breach of the Peace, be privileged from Arrest during their Attendance at the Session of their respective Houses, and in going to and returning from the same; and for any Speech or Debate in either House, they shall not be questioned in any other Place.

No Senator or Representative shall, during the Time for which he was elected, be appointed to any civil Office under the Authority of the United States, which shall have been created, or the Emoluments whereof shall have been encreased during such time; and no Person holding any Office under the United States, shall be a Member of either House during his Continuance in Office.

Section. 7.

All Bills for raising Revenue shall originate in the House of Representatives; but the Senate may propose or concur with Amendments as on other Bills.

Every Bill which shall have passed the House of Representatives and the Senate, shall, before it become a Law, be presented to the President of the United States: If he approve he shall sign it, but if not he shall return it, with his Objections to that House in which it shall have originated, who shall enter the Objections at large on their Journal, and proceed to reconsider it. If after such Reconsideration two thirds of that House shall agree to pass the Bill, it shall be sent, together with the Objections, to the other House, by which it shall likewise be reconsidered, and if approved by two thirds of that House, it shall become a Law. But in all such Cases the Votes of both Houses shall be determined by yeas and Nays, and the Names of the Persons voting for and against the Bill shall be entered on the Journal of each House respectively. If any Bill shall not be returned by the President within ten Days (Sundays excepted) after it shall have been presented to him, the Same shall be a Law, in like Manner as if he had signed it, unless the Congress by their Adjournment prevent its Return, in which Case it shall not be a Law.

Every Order, Resolution, or Vote to which the Concurrence of the Senate and House of Representatives may be necessary (except on a question of Adjournment) shall be presented to the President of the United States; and before the Same shall take Effect, shall be approved by him, or being disapproved by him, shall be repassed by two thirds of the Senate and House of Representatives, according to the Rules and Limitations prescribed in the Case of a Bill.

Section. 8.

The Congress shall have Power To lay and collect Taxes, Duties, Imposts and Excises, to pay the Debts and provide for the common Defence and general Welfare of the United States; but all Duties, Imposts and Excises shall be uniform throughout the United States;

To borrow Money on the credit of the United States;

To regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes;

To establish an uniform Rule of Naturalization, and uniform Laws on the subject of Bankruptcies throughout the United States;

To coin Money, regulate the Value thereof, and of foreign Coin, and fix the Standard of Weights and Measures;

To provide for the Punishment of counterfeiting the Securities and current Coin of the United States;

To establish Post Offices and post Roads;

To promote the Progress of Science and useful Arts, by securing for limited Times to Authors and Inventors the exclusive Right to their respective Writings and Discoveries;

To constitute Tribunals inferior to the supreme Court;

To define and punish Piracies and Felonies committed on the high Seas, and Offences against the Law of Nations;

To declare War, grant Letters of Marque and Reprisal, and make Rules concerning Captures on Land and Water;

To raise and support Armies, but no Appropriation of Money to that Use shall be for a longer Term than two Years;

To provide and maintain a Navy;

To make Rules for the Government and Regulation of the land and naval Forces;

To provide for calling forth the Militia to execute the Laws of the Union, suppress Insurrections and repel Invasions;

To provide for organizing, arming, and disciplining, the Militia, and for governing such Part of them as may be employed in the Service of the United States, reserving to the States respectively, the Appointment of the Officers, and the Authority of training the Militia according to the discipline prescribed by Congress;

To exercise exclusive Legislation in all Cases whatsoever, over such District (not exceeding ten Miles square) as may, by Cession of particular States, and the Acceptance of Congress, become the Seat of the Government of the United States, and to exercise like Authority over all Places purchased by the Consent of the Legislature of the State in which the Same shall be, for the Erection of Forts, Magazines, Arsenals, dock-Yards, and other needful Buildings;--And

To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers, and all other Powers vested by this Constitution in the Government of the United States, or in any Department or Officer thereof.

Section. 9.

The Migration or Importation of such Persons as any of the States now existing shall think proper to admit, shall not be prohibited by the Congress prior to the Year one thousand eight hundred and eight, but a Tax or duty may be imposed on such Importation, not exceeding ten dollars for each Person.

The Privilege of the Writ of Habeas Corpus shall not be suspended, unless when in Cases of Rebellion or Invasion the public Safety may require it.

No Bill of Attainder or ex post facto Law shall be passed.

No Capitation, or other direct, Tax shall be laid, unless in Proportion to the Census or enumeration herein before directed to be taken.

No Tax or Duty shall be laid on Articles exported from any State.

No Preference shall be given by any Regulation of Commerce or Revenue to the Ports of one State over those of another; nor shall Vessels bound to, or from, one State, be obliged to enter, clear, or pay Duties in another.

No Money shall be drawn from the Treasury, but in Consequence of Appropriations made by Law; and a regular Statement and Account of the Receipts and Expenditures of all public Money shall be published from time to time.

No Title of Nobility shall be granted by the United States: And no Person holding any Office of Profit or Trust under them, shall, without the Consent of the Congress, accept of any present, Emolument, Office, or Title, of any kind whatever, from any King, Prince, or foreign State.

Section. 10.

No State shall enter into any Treaty, Alliance, or Confederation; grant Letters of Marque and Reprisal; coin Money; emit Bills of Credit; make any Thing but gold and silver Coin a Tender in Payment of Debts; pass any Bill of Attainder, ex post facto Law, or Law impairing the Obligation of Contracts, or grant any Title of Nobility.

No State shall, without the Consent of the Congress, lay any Imposts or Duties on Imports or Exports, except what may be absolutely necessary for executing it's inspection Laws: and the net Produce of all Duties and Imposts, laid by any State on Imports or Exports, shall be for the Use of the Treasury of the United States; and all such Laws shall be subject to the Revision and Controul of the Congress.

No State shall, without the Consent of Congress, lay any Duty of Tonnage, keep Troops, or Ships of War in time of Peace, enter into any Agreement or Compact with another State, or with a foreign Power, or engage in War, unless actually invaded, or in such imminent Danger as will not admit of delay.

Article. II.

Section. 1.

The executive Power shall be vested in a President of the United States of America. He shall hold his Office during the Term of four Years, and, together with the Vice President, chosen for the same Term, be elected, as follows:

Each State shall appoint, in such Manner as the Legislature thereof may direct, a Number of Electors, equal to the whole Number of Senators and Representatives to which the State may be entitled in the Congress: but no Senator or Representative, or Person holding an Office of Trust or Profit under the United States, shall be appointed an Elector.

The Electors shall meet in their respective States, and vote by Ballot for two Persons, of whom one at least shall not be an Inhabitant of the same State with themselves. And they shall make a List of all the Persons voted for, and of the Number of Votes for each; which List they shall sign and certify, and transmit sealed to the Seat of the Government of the United States, directed to the President of the Senate. The President of the Senate shall, in the Presence of the Senate and House of Representatives, open all the Certificates, and the Votes shall then be counted. The Person having the greatest Number of Votes shall be the President, if such Number be a Majority of the whole Number of Electors appointed; and if there be more than one who have such Majority, and have an equal Number of Votes, then the House of Representatives shall immediately chuse by Ballot one of them for President; and if no Person have a Majority, then from the five highest on the List the said House shall in like Manner chuse the President. But in chusing the President, the Votes shall be taken by States, the Representation from each State having one Vote; A quorum for this purpose shall consist of a Member or Members from two thirds of the States, and a Majority of all the States shall be necessary to a Choice. In every Case, after the Choice of the President, the Person having the greatest Number of Votes of the Electors shall be the Vice President. But if there should remain two or more who have equal Votes, the Senate shall chuse from them by Ballot the Vice President.

The Congress may determine the Time of chusing the Electors, and the Day on which they shall give their Votes; which Day shall be the same throughout the United States.

No Person except a natural born Citizen, or a Citizen of the United States, at the time of the Adoption of this Constitution, shall be eligible to the Office of President; neither shall any Person be eligible to that Office who shall not have attained to the Age of thirty five Years, and been fourteen Years a Resident within the United States.

In Case of the Removal of the President from Office, or of his Death, Resignation, or Inability to discharge the Powers and Duties of the said Office, the Same shall devolve on the Vice President, and the Congress may by Law provide for the Case of Removal, Death, Resignation or Inability, both of the President and Vice President, declaring what Officer shall then act as President, and such Officer shall act accordingly, until the Disability be removed, or a President shall be elected.

The President shall, at stated Times, receive for his Services, a Compensation, which shall neither be increased nor diminished during the Period for which he shall have been elected, and he shall not receive within that Period any other Emolument from the United States, or any of them.

Before he enter on the Execution of his Office, he shall take the following Oath or Affirmation:--"I do solemnly swear (or affirm) that I will faithfully execute the Office of President of the United States, and will to the best of my Ability, preserve, protect and defend the Constitution of the United States."

Section. 2.

The President shall be Commander in Chief of the Army and Navy of the United States, and of the Militia of the several States, when called into the actual Service of the United States; he may require the Opinion, in writing, of the principal Officer in each of the executive Departments, upon any Subject relating to the Duties of their respective Offices, and he shall have Power to grant Reprieves and Pardons for Offences against the United States, except in Cases of Impeachment.

He shall have Power, by and with the Advice and Consent of the Senate, to make Treaties, provided two thirds of the Senators present concur; and he shall nominate, and by and with the Advice and Consent of the Senate, shall appoint Ambassadors, other public Ministers and Consuls, Judges of the supreme Court, and all other Officers of the United States, whose Appointments are not herein otherwise provided for, and which shall be established by Law: but the Congress may by Law vest the Appointment of such inferior Officers, as they think proper, in the President alone, in the Courts of Law, or in the Heads of Departments.

The President shall have Power to fill up all Vacancies that may happen during the Recess of the Senate, by granting Commissions which shall expire at the End of their next Session.

Section. 3.

He shall from time to time give to the Congress Information of the State of the Union, and recommend to their Consideration such Measures as he shall judge necessary and expedient; he may, on extraordinary Occasions, convene both Houses, or either of them, and in Case of Disagreement between them, with Respect to the Time of Adjournment, he may adjourn them to such Time as he shall think proper; he shall receive Ambassadors and other public Ministers; he shall take Care that the Laws be faithfully executed, and shall Commission all the Officers of the United States.

Section. 4.

The President, Vice President and all civil Officers of the United States, shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors.

Article III.

Section. 1.

The judicial Power of the United States shall be vested in one supreme Court, and in such inferior Courts as the Congress may from time to time ordain and establish. The Judges, both of the supreme and inferior Courts, shall hold their Offices during good Behaviour, and shall, at stated Times, receive for their Services a Compensation, which shall not be diminished during their Continuance in Office.

Section. 2.

The judicial Power shall extend to all Cases, in Law and Equity, arising under this Constitution, the Laws of the United States, and Treaties made, or which shall be made, under their Authority;--to all Cases affecting Ambassadors, other public Ministers and Consuls;--to all Cases of admiralty and maritime Jurisdiction;--to Controversies to which the United States shall be a Party;--to Controversies between two or more States;-- between a State and Citizens of another State,--between Citizens of different States,--between Citizens of the same State claiming Lands under Grants of different States, and between a State, or the Citizens thereof, and foreign States, Citizens or Subjects.

In all Cases affecting Ambassadors, other public Ministers and Consuls, and those in which a State shall be Party, the supreme Court shall have original Jurisdiction. In all the other Cases before mentioned, the supreme Court shall have appellate Jurisdiction, both as to Law and Fact, with such Exceptions, and under such Regulations as the Congress shall make.

The Trial of all Crimes, except in Cases of Impeachment, shall be by Jury; and such Trial shall be held in the State where the said Crimes shall have been committed; but when not committed within any State, the Trial shall be at such Place or Places as the Congress may by Law have directed.

Section. 3.

Treason against the United States, shall consist only in levying War against them, or in adhering to their Enemies, giving them Aid and Comfort. No Person shall be convicted of Treason unless on the Testimony of two Witnesses to the same overt Act, or on Confession in open Court.

The Congress shall have Power to declare the Punishment of Treason, but no Attainder of Treason shall work Corruption of Blood, or Forfeiture except during the Life of the Person attainted.

Article. IV.

Section. 1.

Full Faith and Credit shall be given in each State to the public Acts, Records, and judicial Proceedings of every other State. And the Congress may by general Laws prescribe the Manner in which such Acts, Records and Proceedings shall be proved, and the Effect thereof.

Section. 2.

The Citizens of each State shall be entitled to all Privileges and Immunities of Citizens in the several States.

A Person charged in any State with Treason, Felony, or other Crime, who shall flee from Justice, and be found in another State, shall on Demand of the executive Authority of the State from which he fled, be delivered up, to be removed to the State having Jurisdiction of the Crime.

No Person held to Service or Labour in one State, under the Laws thereof, escaping into another, shall, in Consequence of any Law or Regulation therein, be discharged from such Service or Labour, but shall be delivered up on Claim of the Party to whom such Service or Labour may be due.

Section. 3.

New States may be admitted by the Congress into this Union; but no new State shall be formed or erected within the Jurisdiction of any other State; nor any State be formed by the Junction of two or more States, or Parts of States, without the Consent of the Legislatures of the States concerned as well as of the Congress.

The Congress shall have Power to dispose of and make all needful Rules and Regulations respecting the Territory or other Property belonging to the United States; and nothing in this Constitution shall be so construed as to Prejudice any Claims of the United States, or of any particular State.

Section. 4.

The United States shall guarantee to every State in this Union a Republican Form of Government, and shall protect each of them against Invasion; and on Application of the Legislature, or of the Executive (when the Legislature cannot be convened), against domestic Violence.

Article. V.

The Congress, whenever two thirds of both Houses shall deem it necessary, shall propose Amendments to this Constitution, or, on the Application of the Legislatures of two thirds of the several States, shall call a Convention for proposing Amendments, which, in either Case, shall be valid to all Intents and Purposes, as Part of this Constitution, when ratified by the Legislatures of three fourths of the several States, or by Conventions in three fourths thereof, as the one or the other Mode of Ratification may be proposed by the Congress; Provided that no Amendment which may be made prior to the Year One thousand eight hundred and eight shall in any Manner affect the first and fourth Clauses in the Ninth Section of the first Article; and that no State, without its Consent, shall be deprived of its equal Suffrage in the Senate.

Article. VI.

All Debts contracted and Engagements entered into, before the Adoption of this Constitution, shall be as valid against the United States under this Constitution, as under the Confederation.

This Constitution, and the Laws of the United States which shall be made in Pursuance thereof; and all Treaties made, or which shall be made, under the Authority of the United States, shall be the supreme Law of the Land; and the Judges in every State shall be bound thereby, any Thing in the Constitution or Laws of any State to the Contrary notwithstanding.

The Senators and Representatives before mentioned, and the Members of the several State Legislatures, and all executive and judicial Officers, both of the United States and of the several States, shall be bound by Oath or Affirmation, to support this Constitution; but no religious Test shall ever be required as a Qualification to any Office or public Trust under the United States.

Article. VII.

The Ratification of the Conventions of nine States, shall be sufficient for the Establishment of this Constitution between the States so ratifying the Same.

The Word, "the," being interlined between the seventh and eighth Lines of the first Page, the Word "Thirty" being partly written on an Erazure in the fifteenth Line of the first Page, The Words "is tried" being interlined between the thirty second and thirty third Lines of the first Page and the Word "the" being interlined between the forty third and forty fourth Lines of the second Page.

Attest William Jackson Secretary

done in Convention by the Unanimous Consent of the States present the Seventeenth Day of September in the Year of our Lord one thousand seven hundred and Eighty seven and of the Independance of the United States of America the Twelfth In witness whereof We have hereunto subscribed our Names,

Geo. Washington
Presidt and deputy from Virginia

Delaware
Geo: Read
Gunning Bedford jun
John Dickinson
Richard Bassett
Jaco: Broom

Maryland
James McHenry
Dan of St Thos. Jenifer
Danl. Carroll

Virginia
John Blair
James Madison Jr.

North Carolina
Wm. Blount
Richd. Dobbs Spaight
Hu Williamson

South Carolina
J. Rutledge
Charles Cotesworth Pinckney
Charles Pinckney
Pierce Butler

Georgia
William Few
Abr Baldwin

New Hampshire
John Langdon
Nicholas Gilman

Massachusetts
Nathaniel Gorham
Rufus King

Connecticut
Wm. Saml. Johnson
Roger Sherman

New York
Alexander Hamilton

New Jersey
Wil: Livingston
David Brearley
Wm. Paterson
Jona: Dayton

Pennsylvania
B Franklin
Thomas Mifflin
Robt. Morris
Geo. Clymer
Thos. FitzSimons
Jared Ingersoll
James Wilson
Gouv Morris
"""
        
    elif docname == "magna_carta":
        #return "Being that we don't like absolute kings anymore"
        return """Preamble: John, by the grace of God, king of England, lord of Ireland, duke of Normandy and Aquitaine, and count of Anjou, to the archbishop, bishops, abbots, earls, barons, justiciaries, foresters, sheriffs, stewards, servants, and to all his bailiffs and liege subjects, greetings. Know that, having regard to God and for the salvation of our soul, and those of all our ancestors and heirs, and unto the honor of God and the advancement of his holy Church and for the rectifying of our realm, we have granted as underwritten by advice of our venerable fathers, Stephen, archbishop of Canterbury, primate of all England and cardinal of the holy Roman Church, Henry, archbishop of Dublin, William of London, Peter of Winchester, Jocelyn of Bath and Glastonbury, Hugh of Lincoln, Walter of Worcester, William of Coventry, Benedict of Rochester, bishops; of Master Pandulf, subdeacon and member of the household of our lord the Pope, of brother Aymeric (master of the Knights of the Temple in England), and of the illustrious men William Marshal, earl of Pembroke, William, earl of Salisbury, William, earl of Warenne, William, earl of Arundel, Alan of Galloway (constable of Scotland), Waren Fitz Gerold, Peter Fitz Herbert, Hubert De Burgh (seneschal of Poitou), Hugh de Neville, Matthew Fitz Herbert, Thomas Basset, Alan Basset, Philip d'Aubigny, Robert of Roppesley, John Marshal, John Fitz Hugh, and others, our liegemen.

1. In the first place we have granted to God, and by this our present charter confirmed for us and our heirs forever that the English Church shall be free, and shall have her rights entire, and her liberties inviolate; and we will that it be thus observed; which is apparent from this that the freedom of elections, which is reckoned most important and very essential to the English Church, we, of our pure and unconstrained will, did grant, and did by our charter confirm and did obtain the ratification of the same from our lord, Pope Innocent III, before the quarrel arose between us and our barons: and this we will observe, and our will is that it be observed in good faith by our heirs forever. We have also granted to all freemen of our kingdom, for us and our heirs forever, all the underwritten liberties, to be had and held by them and their heirs, of us and our heirs forever.

2. If any of our earls or barons, or others holding of us in chief by military service shall have died, and at the time of his death his heir shall be full of age and owe "relief", he shall have his inheritance by the old relief, to wit, the heir or heirs of an earl, for the whole barony of an earl by 100; the heir or heirs of a baron, 100 for a whole barony; the heir or heirs of a knight, 100s, at most, and whoever owes less let him give less, according to the ancient custom of fees.

3. If, however, the heir of any one of the aforesaid has been under age and in wardship, let him have his inheritance without relief and without fine when he comes of age.

4. The guardian of the land of an heir who is thus under age, shall take from the land of the heir nothing but reasonable produce, reasonable customs, and reasonable services, and that without destruction or waste of men or goods; and if we have committed the wardship of the lands of any such minor to the sheriff, or to any other who is responsible to us for its issues, and he has made destruction or waster of what he holds in wardship, we will take of him amends, and the land shall be committed to two lawful and discreet men of that fee, who shall be responsible for the issues to us or to him to whom we shall assign them; and if we have given or sold the wardship of any such land to anyone and he has therein made destruction or waste, he shall lose that wardship, and it shall be transferred to two lawful and discreet men of that fief, who shall be responsible to us in like manner as aforesaid.

5. The guardian, moreover, so long as he has the wardship of the land, shall keep up the houses, parks, fishponds, stanks, mills, and other things pertaining to the land, out of the issues of the same land; and he shall restore to the heir, when he has come to full age, all his land, stocked with ploughs and wainage, according as the season of husbandry shall require, and the issues of the land can reasonable bear.

6. Heirs shall be married without disparagement, yet so that before the marriage takes place the nearest in blood to that heir shall have notice.

7. A widow, after the death of her husband, shall forthwith and without difficulty have her marriage portion and inheritance; nor shall she give anything for her dower, or for her marriage portion, or for the inheritance which her husband and she held on the day of the death of that husband; and she may remain in the house of her husband for forty days after his death, within which time her dower shall be assigned to her.

8. No widow shall be compelled to marry, so long as she prefers to live without a husband; provided always that she gives security not to marry without our consent, if she holds of us, or without the consent of the lord of whom she holds, if she holds of another.

9. Neither we nor our bailiffs will seize any land or rent for any debt, as long as the chattels of the debtor are sufficient to repay the debt; nor shall the sureties of the debtor be distrained so long as the principal debtor is able to satisfy the debt; and if the principal debtor shall fail to pay the debt, having nothing wherewith to pay it, then the sureties shall answer for the debt; and let them have the lands and rents of the debtor, if they desire them, until they are indemnified for the debt which they have paid for him, unless the principal debtor can show proof that he is discharged thereof as against the said sureties.

10. If one who has borrowed from the Jews any sum, great or small, die before that loan be repaid, the debt shall not bear interest while the heir is under age, of whomsoever he may hold; and if the debt fall into our hands, we will not take anything except the principal sum contained in the bond.

11. And if anyone die indebted to the Jews, his wife shall have her dower and pay nothing of that debt; and if any children of the deceased are left under age, necessaries shall be provided for them in keeping with the holding of the deceased; and out of the residue the debt shall be paid, reserving, however, service due to feudal lords; in like manner let it be done touching debts due to others than Jews.

12. No scutage not aid shall be imposed on our kingdom, unless by common counsel of our kingdom, except for ransoming our person, for making our eldest son a knight, and for once marrying our eldest daughter; and for these there shall not be levied more than a reasonable aid. In like manner it shall be done concerning aids from the city of London.

13. And the city of London shall have all it ancient liberties and free customs, as well by land as by water; furthermore, we decree and grant that all other cities, boroughs, towns, and ports shall have all their liberties and free customs.

14. And for obtaining the common counsel of the kingdom anent the assessing of an aid (except in the three cases aforesaid) or of a scutage, we will cause to be summoned the archbishops, bishops, abbots, earls, and greater barons, severally by our letters; and we will moveover cause to be summoned generally, through our sheriffs and bailiffs, and others who hold of us in chief, for a fixed date, namely, after the expiry of at least forty days, and at a fixed place; and in all letters of such summons we will specify the reason of the summons. And when the summons has thus been made, the business shall proceed on the day appointed, according to the counsel of such as are present, although not all who were summoned have come.

15. We will not for the future grant to anyone license to take an aid from his own free tenants, except to ransom his person, to make his eldest son a knight, and once to marry his eldest daughter; and on each of these occasions there shall be levied only a reasonable aid.

16. No one shall be distrained for performance of greater service for a knight's fee, or for any other free tenement, than is due therefrom.

17. Common pleas shall not follow our court, but shall be held in some fixed place.

18. Inquests of novel disseisin, of mort d'ancestor, and of darrein presentment shall not be held elsewhere than in their own county courts, and that in manner following; We, or, if we should be out of the realm, our chief justiciar, will send two justiciaries through every county four times a year, who shall alone with four knights of the county chosen by the county, hold the said assizes in the county court, on the day and in the place of meeting of that court.

19. And if any of the said assizes cannot be taken on the day of the county court, let there remain of the knights and freeholders, who were present at the county court on that day, as many as may be required for the efficient making of judgments, according as the business be more or less.

20. A freeman shall not be amerced for a slight offense, except in accordance with the degree of the offense; and for a grave offense he shall be amerced in accordance with the gravity of the offense, yet saving always his "contentment"; and a merchant in the same way, saving his "merchandise"; and a villein shall be amerced in the same way, saving his "wainage" if they have fallen into our mercy: and none of the aforesaid amercements shall be imposed except by the oath of honest men of the neighborhood.

21. Earls and barons shall not be amerced except through their peers, and only in accordance with the degree of the offense.

22. A clerk shall not be amerced in respect of his lay holding except after the manner of the others aforesaid; further, he shall not be amerced in accordance with the extent of his ecclesiastical benefice.

23. No village or individual shall be compelled to make bridges at river banks, except those who from of old were legally bound to do so.

24. No sheriff, constable, coroners, or others of our bailiffs, shall hold pleas of our Crown.

25. All counties, hundred, wapentakes, and trithings (except our demesne manors) shall remain at the old rents, and without any additional payment.

26. If anyone holding of us a lay fief shall die, and our sheriff or bailiff shall exhibit our letters patent of summons for a debt which the deceased owed us, it shall be lawful for our sheriff or bailiff to attach and enroll the chattels of the deceased, found upon the lay fief, to the value of that debt, at the sight of law worthy men, provided always that nothing whatever be thence removed until the debt which is evident shall be fully paid to us; and the residue shall be left to the executors to fulfill the will of the deceased; and if there be nothing due from him to us, all the chattels shall go to the deceased, saving to his wife and children their reasonable shares.

27. If any freeman shall die intestate, his chattels shall be distributed by the hands of his nearest kinsfolk and friends, under supervision of the Church, saving to every one the debts which the deceased owed to him.

28. No constable or other bailiff of ours shall take corn or other provisions from anyone without immediately tendering money therefor, unless he can have postponement thereof by permission of the seller.

29. No constable shall compel any knight to give money in lieu of castle-guard, when he is willing to perform it in his own person, or (if he himself cannot do it from any reasonable cause) then by another responsible man. Further, if we have led or sent him upon military service, he shall be relieved from guard in proportion to the time during which he has been on service because of us.

30. No sheriff or bailiff of ours, or other person, shall take the horses or carts of any freeman for transport duty, against the will of the said freeman.

31. Neither we nor our bailiffs shall take, for our castles or for any other work of ours, wood which is not ours, against the will of the owner of that wood.

32. We will not retain beyond one year and one day, the lands those who have been convicted of felony, and the lands shall thereafter be handed over to the lords of the fiefs.

33. All kydells for the future shall be removed altogether from Thames and Medway, and throughout all England, except upon the seashore.

34. The writ which is called praecipe shall not for the future be issued to anyone, regarding any tenement whereby a freeman may lose his court.

35. Let there be one measure of wine throughout our whole realm; and one measure of ale; and one measure of corn, to wit, "the London quarter"; and one width of cloth (whether dyed, or russet, or "halberget"), to wit, two ells within the selvedges; of weights also let it be as of measures.

36. Nothing in future shall be given or taken for a writ of inquisition of life or limbs, but freely it shall be granted, and never denied.

37. If anyone holds of us by fee-farm, either by socage or by burage, or of any other land by knight's service, we will not (by reason of that fee-farm, socage, or burgage), have the wardship of the heir, or of such land of his as if of the fief of that other; nor shall we have wardship of that fee-farm, socage, or burgage, unless such fee-farm owes knight's service. We will not by reason of any small serjeancy which anyone may hold of us by the service of rendering to us knives, arrows, or the like, have wardship of his heir or of the land which he holds of another lord by knight's service.

38. No bailiff for the future shall, upon his own unsupported complaint, put anyone to his "law", without credible witnesses brought for this purposes.

39. No freemen shall be taken or imprisoned or disseised or exiled or in any way destroyed, nor will we go upon him nor send upon him, except by the lawful judgment of his peers or by the law of the land.

40. To no one will we sell, to no one will we refuse or delay, right or justice.

41. All merchants shall have safe and secure exit from England, and entry to England, with the right to tarry there and to move about as well by land as by water, for buying and selling by the ancient and right customs, quit from all evil tolls, except (in time of war) such merchants as are of the land at war with us. And if such are found in our land at the beginning of the war, they shall be detained, without injury to their bodies or goods, until information be received by us, or by our chief justiciar, how the merchants of our land found in the land at war with us are treated; and if our men are safe there, the others shall be safe in our land.

42. It shall be lawful in future for anyone (excepting always those imprisoned or outlawed in accordance with the law of the kingdom, and natives of any country at war with us, and merchants, who shall be treated as if above provided) to leave our kingdom and to return, safe and secure by land and water, except for a short period in time of war, on grounds of public policy- reserving always the allegiance due to us.

43. If anyone holding of some escheat (such as the honor of Wallingford, Nottingham, Boulogne, Lancaster, or of other escheats which are in our hands and are baronies) shall die, his heir shall give no other relief, and perform no other service to us than he would have done to the baron if that barony had been in the baron's hand; and we shall hold it in the same manner in which the baron held it.

44. Men who dwell without the forest need not henceforth come before our justiciaries of the forest upon a general summons, unless they are in plea, or sureties of one or more, who are attached for the forest.

45. We will appoint as justices, constables, sheriffs, or bailiffs only such as know the law of the realm and mean to observe it well.

46. All barons who have founded abbeys, concerning which they hold charters from the kings of England, or of which they have long continued possession, shall have the wardship of them, when vacant, as they ought to have.

47. All forests that have been made such in our time shall forthwith be disafforsted; and a similar course shall be followed with regard to river banks that have been placed "in defense" by us in our time.

48. All evil customs connected with forests and warrens, foresters and warreners, sheriffs and their officers, river banks and their wardens, shall immediately by inquired into in each county by twelve sworn knights of the same county chosen by the honest men of the same county, and shall, within forty days of the said inquest, be utterly abolished, so as never to be restored, provided always that we previously have intimation thereof, or our justiciar, if we should not be in England.

49. We will immediately restore all hostages and charters delivered to us by Englishmen, as sureties of the peace of faithful service.

50. We will entirely remove from their bailiwicks, the relations of Gerard of Athee (so that in future they shall have no bailiwick in England); namely, Engelard of Cigogne, Peter, Guy, and Andrew of Chanceaux, Guy of Cigogne, Geoffrey of Martigny with his brothers, Philip Mark with his brothers and his nephew Geoffrey, and the whole brood of the same.

51. As soon as peace is restored, we will banish from the kingdom all foreign born knights, crossbowmen, serjeants, and mercenary soldiers who have come with horses and arms to the kingdom's hurt.

52. If anyone has been dispossessed or removed by us, without the legal judgment of his peers, from his lands, castles, franchises, or from his right, we will immediately restore them to him; and if a dispute arise over this, then let it be decided by the five and twenty barons of whom mention is made below in the clause for securing the peace. Moreover, for all those possessions, from which anyone has, without the lawful judgment of his peers, been disseised or removed, by our father, King Henry, or by our brother, King Richard, and which we retain in our hand (or which as possessed by others, to whom we are bound to warrant them) we shall have respite until the usual term of crusaders; excepting those things about which a plea has been raised, or an inquest made by our order, before our taking of the cross; but as soon as we return from the expedition, we will immediately grant full justice therein.

53. We shall have, moreover, the same respite and in the same manner in rendering justice concerning the disafforestation or retention of those forests which Henry our father and Richard our broter afforested, and concerning the wardship of lands which are of the fief of another (namely, such wardships as we have hitherto had by reason of a fief which anyone held of us by knight's service), and concerning abbeys founded on other fiefs than our own, in which the lord of the fee claims to have right; and when we have returned, or if we desist from our expedition, we will immediately grant full justice to all who complain of such things.

54. No one shall be arrested or imprisoned upon the appeal of a woman, for the death of any other than her husband.

55. All fines made with us unjustly and against the law of the land, and all amercements, imposed unjustly and against the law of the land, shall be entirely remitted, or else it shall be done concerning them according to the decision of the five and twenty barons whom mention is made below in the clause for securing the pease, or according to the judgment of the majority of the same, along with the aforesaid Stephen, archbishop of Canterbury, if he can be present, and such others as he may wish to bring with him for this purpose, and if he cannot be present the business shall nevertheless proceed without him, provided always that if any one or more of the aforesaid five and twenty barons are in a similar suit, they shall be removed as far as concerns this particular judgment, others being substituted in their places after having been selected by the rest of the same five and twenty for this purpose only, and after having been sworn.

56. If we have disseised or removed Welshmen from lands or liberties, or other things, without the legal judgment of their peers in England or in Wales, they shall be immediately restored to them; and if a dispute arise over this, then let it be decided in the marches by the judgment of their peers; for the tenements in England according to the law of England, for tenements in Wales according to the law of Wales, and for tenements in the marches according to the law of the marches. Welshmen shall do the same to us and ours.

57. Further, for all those possessions from which any Welshman has, without the lawful judgment of his peers, been disseised or removed by King Henry our father, or King Richard our brother, and which we retain in our hand (or which are possessed by others, and which we ought to warrant), we will have respite until the usual term of crusaders; excepting those things about which a plea has been raised or an inquest made by our order before we took the cross; but as soon as we return (or if perchance we desist from our expedition), we will immediately grant full justice in accordance with the laws of the Welsh and in relation to the foresaid regions.

58. We will immediately give up the son of Llywelyn and all the hostages of Wales, and the charters delivered to us as security for the peace.

59. We will do towards Alexander, king of Scots, concerning the return of his sisters and his hostages, and concerning his franchises, and his right, in the same manner as we shall do towards our owher barons of England, unless it ought to be otherwise according to the charters which we hold from William his father, formerly king of Scots; and this shall be according to the judgment of his peers in our court.

60. Moreover, all these aforesaid customs and liberties, the observances of which we have granted in our kingdom as far as pertains to us towards our men, shall be observed b all of our kingdom, as well clergy as laymen, as far as pertains to them towards their men.

61. Since, moveover, for God and the amendment of our kingdom and for the better allaying of the quarrel that has arisen between us and our barons, we have granted all these concessions, desirous that they should enjoy them in complete and firm endurance forever, we give and grant to them the underwritten security, namely, that the barons choose five and twenty barons of the kingdom, whomsoever they will, who shall be bound with all their might, to observe and hold, and cause to be observed, the peace and liberties we have granted and confirmed to them by this our present Charter, so that if we, or our justiciar, or our bailiffs or any one of our officers, shall in anything be at fault towards anyone, or shall have broken any one of the articles of this peace or of this security, and the offense be notified to four barons of the foresaid five and twenty, the said four barons shall repair to us (or our justiciar, if we are out of the realm) and, laying the transgression before us, petition to have that transgression redressed without delay. And if we shall not have corrected the transgression (or, in the event of our being out of the realm, if our justiciar shall not have corrected it) within forty days, reckoning from the time it has been intimated to us (or to our justiciar, if we should be out of the realm), the four barons aforesaid shall refer that matter to the rest of the five and twenty barons, and those five and twenty barons shall, together with the community of the whole realm, distrain and distress us in all possible ways, namely, by seizing our castles, lands, possessions, and in any other way they can, until redress has been obtained as they deem fit, saving harmless our own person, and the persons of our queen and children; and when redress has been obtained, they shall resume their old relations towards us. And let whoever in the country desires it, swear to obey the orders of the said five and twenty barons for the execution of all the aforesaid matters, and along with them, to molest us to the utmost of his power; and we publicly and freely grant leave to everyone who wishes to swear, and we shall never forbid anyone to swear. All those, moveover, in the land who of themselves and of their own accord are unwilling to swear to the twenty five to help them in constraining and molesting us, we shall by our command compel the same to swear to the effect foresaid. And if any one of the five and twenty barons shall have died or departed from the land, or be incapacitated in any other manner which would prevent the foresaid provisions being carried out, those of the said twenty five barons who are left shall choose another in his place according to their own judgment, and he shall be sworn in the same way as the others. Further, in all matters, the execution of which is entrusted,to these twenty five barons, if perchance these twenty five are present and disagree about anything, or if some of them, after being summoned, are unwilling or unable to be present, that which the majority of those present ordain or command shall be held as fixed and established, exactly as if the whole twenty five had concurred in this; and the said twenty five shall swear that they will faithfully observe all that is aforesaid, and cause it to be observed with all their might. And we shall procure nothing from anyone, directly or indirectly, whereby any part of these concessions and liberties might be revoked or diminished; and if any such things has been procured, let it be void and null, and we shall never use it personally or by another.

62. And all the will, hatreds, and bitterness that have arisen between us and our men, clergy and lay, from the date of the quarrel, we have completely remitted and pardoned to everyone. Moreover, all trespasses occasioned by the said quarrel, from Easter in the sixteenth year of our reign till the restoration of peace, we have fully remitted to all, both clergy and laymen, and completely forgiven, as far as pertains to us. And on this head, we have caused to be made for them letters testimonial patent of the lord Stephen, archbishop of Canterbury, of the lord Henry, archbishop of Dublin, of the bishops aforesaid, and of Master Pandulf as touching this security and the concessions aforesaid.

63. Wherefore we will and firmly order that the English Church be free, and that the men in our kingdom have and hold all the aforesaid liberties, rights, and concessions, well and peaceably, freely and quietly, fully and wholly, for themselves and their heirs, of us and our heirs, in all respects and in all places forever, as is aforesaid. An oath, moreover, has been taken, as well on our part as on the art of the barons, that all these conditions aforesaid shall be kept in good faith and without evil intent.

Given under our hand - the above named and many others being witnesses - in the meadow which is called Runnymede, between Windsor and Staines, on the fifteenth day of June, in the seventeenth year of our reign.
"""
        
    elif docname == "un_charter":
        #return "The charter of the United Nations begins like this"
        return """==Preamble==
WE THE PEOPLES OF THE UNITED NATIONS DETERMINED
* to save succeeding generations from the scourge of war, which twice in our lifetime has brought untold sorrow to mankind, and
* to reaffirm faith in fundamental human rights, in the dignity and worth of the human person, in the equal rights of men and women and of nations large and small, and
* to establish conditions under which justice and respect for the obligations arising from treaties and other sources of international law can be maintained, and
* to promote social progress and better standards of life in larger freedom,
AND FOR THESE ENDS
* to practice tolerance and live together in peace with one another as good neighbours, and
* to unite our strength to maintain international peace and security, and
* to ensure, by the acceptance of principles and the institution of methods, that armed force shall not be used, save in the common interest, and
* to employ international machinery for the promotion of the economic and social advancement of all peoples,
HAVE RESOLVED TO COMBINE OUR EFFORTS TO ACCOMPLISH THESE AIMS<br>
Accordingly, our respective Governments, through representatives assembled in the city of San Francisco, who have exhibited their full powers found to be in good and due form, have agreed to the present Charter of the United Nations and do hereby establish an international organization to be known as the United Nations.
==Chapter I - Purposes and Principles==
===Article 1===
The Purposes of the United Nations are:
# To maintain international peace and security, and to that end: to take effective collective measures for the prevention and removal of threats to the peace, and for the suppression of acts of aggression or other breaches of the peace, and to bring about by peaceful means, and in conformity with the principles of justice and international law, adjustment or settlement of international disputes or situations which might lead to a breach of the peace;
# To develop friendly relations among nations based on respect for the principle of equal rights and self-determination of peoples, and to take other appropriate measures to strengthen universal peace;
# To achieve international co-operation in solving international problems of an economic, social, cultural, or humanitarian character, and in promoting and encouraging respect for human rights and for fundamental freedoms for all without distinction as to race, sex, language, or religion; and
# To be a centre for harmonizing the actions of nations in the attainment of these common ends.

===Article 2===
The Organization and its Members, in pursuit of the Purposes stated in Article 1, shall act in accordance with the following Principles.
# The Organization is based on the principle of the sovereign equality of all its Members.
# All Members, in order to ensure to all of them the rights and benefits resulting from membership, shall fulfill in good faith the obligations assumed by them in accordance with the present Charter.
# All Members shall settle their international disputes by peaceful means in such a manner that international peace and security, and justice, are not endangered.
# All Members shall refrain in their international relations from the threat or use of force against the territorial integrity or political independence of any state, or in any other manner inconsistent with the Purposes of the United Nations.
# All Members shall give the United Nations every assistance in any action it takes in accordance with the present Charter, and shall refrain from giving assistance to any state against which the United Nations is taking preventive or enforcement action.
# The Organization shall ensure that states which are not Members of the United Nations act in accordance with these Principles so far as may be necessary for the maintenance of international peace and security.
# Nothing contained in the present Charter shall authorize the United Nations to intervene in matters which are essentially within the domestic jurisdiction of any state or shall require the Members to submit such matters to settlement under the present Charter; but this principle shall not prejudice the application of enforcement measures under Chapter VII.

==Chapter II - Membership==
===Article 3===
The original Members of the United Nations shall be the states which, having participated in the United Nations Conference on International Organization at San Francisco, or having previously signed the Declaration by United Nations of 1 January 1942, sign the present Charter and ratify it in accordance with Article 110.
===Article 4===
# Membership in the United Nations is open to all other peace-loving states which accept the obligations contained in the present Charter and, in the judgment of the Organization, are able and willing to carry out these obligations.
# The admission of any such state to membership in the United Nations will be effected by a decision of the General Assembly upon the recommendation of the Security Council.
===Article 5===
A Member of the United Nations against which preventive or enforcement action has been taken by the Security Council may be suspended from the exercise of the rights and privileges of membership by the General Assembly upon the recommendation of the Security Council. The exercise of these rights and privileges may be restored by the Security Council.
===Article 6===
A Member of the United Nations which has persistently violated the Principles contained in the present Charter may be expelled from the Organization by the General Assembly upon the recommendation of the Security Council.
==Chapter III - Organs==
===Article 7===
# There are established as the principal organs of the United Nations:
::* a General Assembly
::* a Security Council
::* an Economic and Social Council
::* a Trusteeship Council
::* an International Court of Justice
::* and a Secretariat.
:2. Such subsidiary organs as may be found necessary may be established in accordance with the present Charter.
===Article 8===
The United Nations shall place no restrictions on the eligibility of men and women to participate in any capacity and under conditions of equality in its principal and subsidiary organs.
==Chapter IV - The General Assembly==
===Composition===
====Article 9====
# The General Assembly shall consist of all the Members of the United Nations.
# Each Member shall have not more than five representatives in the General Assembly.
===Functions and Powers===
====Article 10====
The General Assembly may discuss any questions or any matters within the scope of the present Charter or relating to the powers and functions of any organs provided for in the present Charter, and, except as provided in Article 12, may make recommendations to the Members of the United Nations or to the Security Council or to both on any such questions or matters.
====Article 11====
# The General Assembly may consider the general principles of co-operation in the maintenance of international peace and security, including the principles governing disarmament and the regulation of armaments, and may make recommendations with regard to such principles to the Members or to the Security Council or to both.
# The General Assembly may discuss any questions relating to the maintenance of international peace and security brought before it by any Member of the United Nations, or by the Security Council, or by a state which is not a Member of the United Nations in accordance with Article 35, paragraph 2, and, except as provided in Article 12, may make recommendations with regard to any such questions to the state or states concerned or to the Security Council or to both. Any such question on which action is necessary shall be referred to the Security Council by the General Assembly either before or after discussion.
# The General Assembly may call the attention of the Security Council to situations which are likely to endanger international peace and security.
# The powers of the General Assembly set forth in this Article shall not limit the general scope of Article 10.
====Article 12====
# While the Security Council is exercising in respect of any dispute or situation the functions assigned to it in the present Charter, the General Assembly shall not make any recommendation with regard to that dispute or situation unless the Security Council so requests.
# The Secretary-General, with the consent of the Security Council, shall notify the General Assembly at each session of any matters relative to the maintenance of international peace and security which are being dealt with by the Security Council and shall similarly notify the General Assembly, or the Members of the United Nations if the General Assembly is not in session, immediately the Security Council ceases to deal with such matters.
====Article 13====
# The General Assembly shall initiate studies and make recommendations for the purpose of: :a. promoting international co-operation in the political field and encouraging the progressive development of international law and its codification; :b. promoting international co-operation in the economic, social, cultural, educational, and health fields, and assisting in the realization of human rights and fundamental freedoms for all without distinction as to race, sex, language, or religion.
# The further responsibilities, functions and powers of the General Assembly with respect to matters mentioned in paragraph 1 (b) above are set forth in Chapters IX and X.
====Article 14====
Subject to the provisions of Article 12, the General Assembly may recommend measures for the peaceful adjustment of any situation, regardless of origin, which it deems likely to impair the general welfare or friendly relations among nations, including situations resulting from a violation of the provisions of the present Charter setting forth the Purposes and Principles of the United Nations.
====Article 15====
# The General Assembly shall receive and consider annual and special reports from the Security Council; these reports shall include an account of the measures that the Security Council has decided upon or taken to maintain international peace and security.
# The General Assembly shall receive and consider reports from the other organs of the United Nations.
====Article 16====
The General Assembly shall perform such functions with respect to the international trusteeship system as are assigned to it under Chapters XII and XIII, including the approval of the trusteeship agreements for areas not designated as strategic.
====Article 17====
# The General Assembly shall consider and approve the budget of the Organization.
# The expenses of the Organization shall be borne by the Members as apportioned by the General Assembly.
# The General Assembly shall consider and approve any financial and budgetary arrangements with specialized agencies referred to in Article 57 and shall examine the administrative budgets of such specialized agencies with a view to making recommendations to the agencies concerned.
===Voting===
====Article 18====
# Each member of the General Assembly shall have one vote.
# Decisions of the General Assembly on important questions shall be made by a two-thirds majority of the members present and voting. These questions shall include: recommendations with respect to the maintenance of international peace and security, the election of the non-permanent members of the Security Council, the election of the members of the Economic and Social Council, the election of members of the Trusteeship Council in accordance with paragraph 1 (c) of Article 86, the admission of new Members to the United Nations, the suspension of the rights and privileges of membership, the expulsion of Members, questions relating to the operation of the trusteeship system, and budgetary questions.
# Decisions on other questions, including the determination of additional categories of questions to be decided by a two-thirds majority, shall be made by a majority of the members present and voting.
====Article 19====
A Member of the United Nations which is in arrears in the payment of its financial contributions to the Organization shall have no vote in the General Assembly if the amount of its arrears equals or exceeds the amount of the contributions due from it for the preceding two full years. The General Assembly may, nevertheless, permit such a Member to vote if it is satisfied that the failure to pay is due to conditions beyond the control of the Member.
===Procedure===
====Article 20====
The General Assembly shall meet in regular annual sessions and in such special sessions as occasion may require. Special sessions shall be convoked by the Secretary-General at the request of the Security Council or of a majority of the Members of the United Nations.
====Article 21====
The General Assembly shall adopt its own rules of procedure. It shall elect its President for each session.
====Article 22====
The General Assembly may establish such subsidiary organs as it deems necessary for the performance of its functions.

==Chapter V - The Security Council==
===Composition===
====Article 23====
# The Security Council shall consist of fifteen Members of the United Nations. The Republic of China, France, the Union of Soviet Socialist Republics, the United Kingdom of Great Britain and Northern Ireland, and the United States of America shall be permanent members of the Security Council. The General Assembly shall elect ten other Members of the United Nations to be non-permanent members of the Security Council, due regard being specially paid, in the first instance to the contribution of Members of the United Nations to the maintenance of international peace and security and to the other purposes of the Organization, and also to equitable geographical distribution.
# The non-permanent members of the Security Council shall be elected for a term of two years. In the first election of the non-permanent members after the increase of the membership of the Security Council from eleven to fifteen, two of the four additional members shall be chosen for a term of one year. A retiring member shall not be eligible for immediate re-election.
# Each member of the Security Council shall have one representative.
===Functions and Powers===
====Article 24====
# In order to ensure prompt and effective action by the United Nations, its Members confer on the Security Council primary responsibility for the maintenance of international peace and security, and agree that in carrying out its duties under this responsibility the Security Council acts on their behalf.
# In discharging these duties the Security Council shall act in accordance with the Purposes and Principles of the United Nations. The specific powers granted to the Security Council for the discharge of these duties are laid down in Chapters VI, VII, VIII, and XII.
# The Security Council shall submit annual and, when necessary, special reports to the General Assembly for its consideration.
====Article 25====
The Members of the United Nations agree to accept and carry out the decisions of the Security Council in accordance with the present Charter.
====Article 26====
In order to promote the establishment and maintenance of international peace and security with the least diversion for armaments of the world's human and economic resources, the Security Council shall be responsible for formulating, with the assistance of the Military Staff Committee referred to in Article 47, plans to be submitted to the Members of the United Nations for the establishment of a system for the regulation of armaments.
===Voting===
====Article 27====
# Each member of the Security Council shall have one vote.
# Decisions of the Security Council on procedural matters shall be made by an affirmative vote of nine members.
# Decisions of the Security Council on all other matters shall be made by an affirmative vote of nine members including the concurring votes of the permanent members; provided that, in decisions under Chapter VI, and under paragraph 3 of Article 52, a party to a dispute shall abstain from voting.
===Procedure===
====Article 28====
# The Security Council shall be so organized as to be able to function continuously. Each member of the Security Council shall for this purpose be represented at all times at the seat of the Organization.
# The Security Council shall hold periodic meetings at which each of its members may, if it so desires, be represented by a member of the government or by some other specially designated representative.
# The Security Council may hold meetings at such places other than the seat of the Organization as in its judgment will best facilitate its work.
====Article 29====
The Security Council may establish such subsidiary organs as it deems necessary for the performance of its functions.
====Article 30====
The Security Council shall adopt its own rules of procedure, including the method of selecting its President.
====Article 31====
Any Member of the United Nations which is not a member of the Security Council may participate, without vote, in the discussion of any question brought before the Security Council whenever the latter considers that the interests of that Member are specially affected.
====Article 32====
Any Member of the United Nations which is not a member of the Security Council or any state which is not a Member of the United Nations, if it is a party to a dispute under consideration by the Security Council, shall be invited to participate, without vote, in the discussion relating to the dispute. The Security Council shall lay down such conditions as it deems just for the participation of a state which is not a Member of the United Nations.
==Chapter VI - Pacific Settlement of Disputes==
#REDIRECT[[]]===Article 33===
# The parties to any dispute, the continuance of which is likely to endanger the maintenance of international peace and security, shall, first of all, seek a solution by negotiation, enquiry, mediation, conciliation, arbitration, judicial settlement, resort to regional agencies or arrangements, or other peaceful means of their own choice.
# The Security Council shall, when it deems necessary, call upon the parties to settle their dispute by such means.

===Article 34===
The Security Council may investigate any dispute, or any situation which might lead to international friction or give rise to a dispute, in order to determine whether the continuance of the dispute or situation is likely to endanger the maintenance of international peace and security.
===Article 35===
# Any Member of the United Nations may bring any dispute, or any situation of the nature referred to in Article 34, to the attention of the Security Council or of the General Assembly.
# A state which is not a Member of the United Nations may bring to the attention of the Security Council or of the General Assembly any dispute to which it is a party if it accepts in advance, for the purposes of the dispute, the obligations of pacific settlement provided in the present Charter.
# The proceedings of the General Assembly in respect of matters brought to its attention under this Article will be subject to the provisions of Articles 11 and 12.
===Article 36===
# The Security Council may, at any stage of a dispute of the nature referred to in Article 33 or of a situation of like nature, recommend appropriate procedures or methods of adjustment.
# The Security Council should take into consideration any procedures for the settlement of the dispute which have already been adopted by the parties.
# In making recommendations under this Article the Security Council should also take into consideration that legal disputes should as a general rule be referred by the parties to the International Court of Justice in accordance with the provisions of the Statute of the Court.
===Article 37===
# Should the parties to a dispute of the nature referred to in Article 33 fail to settle it by the means indicated in that Article, they shall refer it to the Security Council.

# If the Security Council deems that the continuance of the dispute is in fact likely to endanger the maintenance of international peace and security, it shall decide whether to take action under Article 36 or to recommend such terms of settlement as it may consider appropriate
===Article 38===
Without prejudice to the provisions of Articles 33 to 37, the Security Council may, if all the parties to any dispute so request, make recommendations to the parties with a view to a pacific settlement of the dispute.
==Chapter VII - Action with Respect to Threats to the Peace, Breaches of the Peace and Acts of Aggression==
===Article 39===
The Security Council shall determine the existence of any threat to the peace, breach of the peace, or act of aggression and shall make recommendations, or decide what measures shall be taken in accordance with Articles 41 and 42, to maintain or restore international peace and security.
===Article 40===
In order to prevent an aggravation of the situation, the Security Council may, before making the recommendations or deciding upon the measures provided for in Article 39, call upon the parties concerned to comply with such provisional measures as it deems necessary or desirable. Such provisional measures shall be without prejudice to the rights, claims, or position of the parties concerned. The Security Council shall duly take account of failure to comply with such provisional measures.
===Article 41===
The Security Council may decide what measures not involving the use of armed force are to be employed to give effect to its decisions, and it may call upon the Members of the United Nations to apply such measures.
These may include complete or partial interruption of economic relations and of rail, sea, air, postal, telegraphic, radio, and other means of communication, and the severance of diplomatic relations.
===Article 42===
Should the Security Council consider that measures provided for in Article 41 would be inadequate or have proved to be inadequate, it may take such action by air, sea, or land forces as may be necessary to maintain or restore international peace and security. Such action may include demonstrations, blockade, and other operations by air, sea, or land forces of Members of the United Nations.
===Article 43===
# All Members of the United Nations, in order to contribute to the maintenance of international peace and security, undertake to make available to the Security Council, on its call and in accordance with a special agreement or agreements, armed forces, assistance, and facilities, including rights of passage, necessary for the purpose of maintaining international peace and security.
# Such agreement or agreements shall govern the numbers and types of forces, their degree of readiness and general location, and the nature of the facilities and assistance to be provided.
# The agreement or agreements shall be negotiated as soon as possible on the initiative of the Security Council. They shall be concluded between the Security Council and Members or between the Security Council and groups of Members and shall be subject to ratification by the signatory states in accordance with their respective constitutional processes.
===Article 44===
When the Security Council has decided to use force it shall, before calling upon a Member not represented on it to provide armed forces in fulfilment of the obligations assumed under Article 43, invite that Member, if the Member so desires, to participate in the decisions of the Security Council concerning the employment of contingents of that Member's armed forces.
===Article 45===
In order to enable the United Nations to take urgent military measures, Members shall hold immediately available national air-force contingents for combined international enforcement action. The strength and degree of readiness of these contingents and plans for their combined action shall be determined within the limits laid down in the special agreement or agreements referred to in Article 43, by the Security Council with the assistance of the Military Staff Committee.
===Article 46===
Plans for the application of armed force shall be made by the Security Council with the assistance of the Military Staff Committee.
===Article 47===
# There shall be established a Military Staff Committee to advise and assist the Security Council on all questions relating to the Security Council's military requirements for the maintenance of international peace and security, the employment and command of forces placed at its disposal, the regulation of armaments, and possible disarmament.
# The Military Staff Committee shall consist of the Chiefs of Staff of the permanent members of the Security Council or their representatives.
Any Member of the United Nations not permanently represented on the Committee shall be invited by the Committee to be associated with it when the efficient discharge of the Committee's responsibilities requires the participation of that Member in its work.
# The Military Staff Committee shall be responsible under the Security Council for the strategic direction of any armed forces placed at the disposal of the Security Council. Questions relating to the command of such forces shall be worked out subsequently.
# The Military Staff Committee, with the authorization of the Security Council and after consultation with appropriate regional agencies, may establish regional sub-committees.
===Article 48===
# The action required to carry out the decisions of the Security Council for the maintenance of international peace and security shall be taken by all the Members of the United Nations or by some of them, as the Security Council may determine.
# Such decisions shall be carried out by the Members of the United Nations directly and through their action in the appropriate international agencies of which they are members.
===Article 49===
The Members of the United Nations shall join in affording mutual assistance in carrying out the measures decided upon by the Security Council.
===Article 50===
If preventive or enforcement measures against any state are taken by the Security Council, any other state, whether a Member of the United Nations or not, which finds itself confronted with special economic problems arising from the carrying out of those measures shall have the right to consult the Security Council with regard to a solution of those problems.
===Article 51===
Nothing in the present Charter shall impair the inherent right of individual or collective self-defense if an armed attack occurs against a Member of the United Nations, until the Security Council has taken measures necessary to maintain international peace and security.
Measures taken by Members in the exercise of this right of self-defense shall be immediately reported to the Security Council and shall not in any way affect the authority and responsibility of the Security Council under the present Charter to take at any time such action as it deems necessary in order to maintain or restore international peace and security.
==Chapter VIII - Regional Arrangements==
===Article 52===
# Nothing in the present Charter precludes the existence of regional arrangements or agencies for dealing with such matters relating to the maintenance of international peace and security as are appropriate for regional action provided that such arrangements or agencies and their activities are consistent with the Purposes and Principles of the United Nations.
# The Members of the United Nations entering into such arrangements or constituting such agencies shall make every effort to achieve pacific settlement of local disputes through such regional arrangements or by such regional agencies before referring them to the Security Council.
# The Security Council shall encourage the development of pacific settlement of local disputes through such regional arrangements or by such regional agencies either on the initiative of the states concerned or by reference from the Security Council.
# This Article in no way impairs the application of Articles 34 and 35.

===Article 53===
# The Security Council shall, where appropriate, utilize such regional arrangements or agencies for enforcement action under its authority. But no enforcement action shall be taken under regional arrangements or by regional agencies without the authorization of the Security Council, with the exception of measures against any enemy state, as defined in paragraph 2 of this Article, provided for pursuant to Article 107 or in regional arrangements directed against renewal of aggressive policy on the part of any such state, until such time as the Organization may, on request of the Governments concerned, be charged with the responsibility for preventing further aggression by such a state.
# The term enemy state as used in paragraph 1 of this Article applies to any state which during the Second World War has been an enemy of any signatory of the present Charter.

===Article 54===
The Security Council shall at all times be kept fully informed of activities undertaken or in contemplation under regional arrangements or by regional agencies for the maintenance of international peace and security.

==Chapter IX - International Economic and Social Co-operation==
===Article 55===
With a view to the creation of conditions of stability and well-being which are necessary for peaceful and friendly relations among nations based on respect for the principle of equal rights and self-determination of peoples, the United Nations shall promote: :a. higher standards of living, full employment, and conditions of economic and social progress and development; :b. solutions of international economic, social, health, and related problems; and international cultural and educational cooperation; and :c. universal respect for, and observance of, human rights and fundamental freedoms for all without distinction as to race, sex, language, or religion.
===Article 56===
All Members pledge themselves to take joint and separate action in co-operation with the Organization for the achievement of the purposes set forth in Article 55.
===Article 57===
# The various specialized agencies, established by intergovernmental agreement and having wide international responsibilities, as defined in their basic instruments, in economic, social, cultural, educational, health, and related fields, shall be brought into relationship with the United Nations in accordance with the provisions of Article 63.
# Such agencies thus brought into relationship with the United Nations are hereinafter referred to as specialized agencies.
===Article 58===
The Organization shall make recommendations for the co-ordination of the policies and activities of the specialized agencies.
===Article 59===
The Organization shall, where appropriate, initiate negotiations among the states concerned for the creation of any new specialized agencies required for the accomplishment of the purposes set forth in Article 55.
===Article 60===
Responsibility for the discharge of the functions of the Organization set forth in this Chapter shall be vested in the General Assembly and, under the authority of the General Assembly, in the Economic and Social Council, which shall have for this purpose the powers set forth in Chapter X.
==Chapter X - The Economic and Social Council==
===Composition===
====Article 61====
# The Economic and Social Council shall consist of fifty-four Members of the United Nations elected by the General Assembly.
# Subject to the provisions of paragraph 3, eighteen members of the Economic and Social Council shall be elected each year for a term of three years. A retiring member shall be eligible for immediate re-election.
# At the first election after the increase in the membership of the Economic and Social Council from twenty-seven to fifty-four members, in addition to the members elected in place of the nine members whose term of office expires at the end of that year, twenty-seven additional members shall be elected. Of these twenty-seven additional members, the term of office of nine members so elected shall expire at the end of one year, and of nine other members at the end of two years, in accordance with arrangements made by the General Assembly.
# Each member of the Economic and Social Council shall have one representative.
===Functions and Powers===
====Article 62====
# The Economic and Social Council may make or initiate studies and reports with respect to international economic, social, cultural, educational, health, and related matters and may make recommendations with respect to any such matters to the General Assembly to the Members of the United Nations, and to the specialized agencies concerned.
# It may make recommendations for the purpose of promoting respect for, and observance of, human rights and fundamental freedoms for all.
# It may prepare draft conventions for submission to the General Assembly, with respect to matters falling within its competence.
# It may call, in accordance with the rules prescribed by the United Nations,international conferences on matters falling within its competence.
====Article 63====
# The Economic and Social Council may enter into agreements with any of the agencies referred to in Article 57, defining the terms on which the agency concerned shall be brought into relationship with the United Nations. Such agreements shall be subject to approval by the General Assembly.
# It may co-ordinate the activities of the specialized agencies through consultation with and recommendations to such agencies and through recommendations to the General Assembly and to the Members of the United Nations.
====Article 64====
# The Economic and Social Council may take appropriate steps to obtain regular reports from the specialized agencies. It may make arrangements with the Members of the United Nations and with the specialized agencies to obtain reports on the steps taken to give effect to its own recommendations and to recommendations on matters falling within its competence made by the General Assembly.
# It may communicate its observations on these reports to the General Assembly.
====Article 65====
The Economic and Social Council may furnish information to the Security Council and shall assist the Security Council upon its request.
====Article 66====
# The Economic and Social Council shall perform such functions as fall within its competence in connexion with the carrying out of the recommendations of the General Assembly.
# It may, with the approval of the General Assembly, perform services at the request of Members of the United Nations and at the request of specialized agencies.
# It shall perform such other functions as are specified elsewhere in the present Charter or as may be assigned to it by the General Assembly.
===Voting===
====Article 67====
# Each member of the Economic and Social Council shall have one vote.
# Decisions of the Economic and Social Council shall be made by a majority of the members present and voting.
===Procedure===
====Article 68====
The Economic and Social Council shall set up commissions in economic and social fields and for the promotion of human rights, and such other commissions as may be required for the performance of its functions.
====Article 69====
The Economic and Social Council shall invite any Member of the United Nations to participate, without vote, in its deliberations on any matter of particular concern to that Member.
====Article 70====
The Economic and Social Council may make arrangements for representatives of the specialized agencies to participate, without vote, in its deliberations and in those of the commissions established by it, and for its representatives to participate in the deliberations of the specialized agencies.
====Article 71====
The Economic and Social Council may make suitable arrangements for consultation with non-governmental organizations which are concerned with matters within its competence. Such arrangements may be made with international organizations and, where appropriate, with national organizations after consultation with the Member of the United Nations concerned.
====Article 72====
# The Economic and Social Council shall adopt its own rules of procedure, including the method of selecting its President.
# The Economic and Social Council shall meet as required in accordance with its rules, which shall include provision for the convening of meetings on the request of a majority of its members.
==Chapter XI - Declaration Regarding Non-Self-Governing Territories==
===Article 73===
Members of the United Nations which have or assume responsibilities for the administration of territories whose peoples have not yet attained a full measure of self-government recognize the principle that the interests of the inhabitants of these territories are paramount, and accept as a sacred trust the obligation to promote to the utmost, within the system of international peace and security established by the present Charter, the well-being of the inhabitants of these territories, and, to this end: :a. to ensure, with due respect for the culture of the peoples concerned, their political, economic, social, and educational advancement, their just treatment, and their protection against abuses; :b. to develop self-government, to take due account of the political aspirations of the peoples, and to assist them in the progressive development of their free political institutions, according to the particular circumstances of each territory and its peoples and their varying stages of advancement; :c. to further international peace and security; :d. to promote constructive measures of development, to encourage research, and to co-operate with one another and, when and where appropriate, with specialized international bodies with a view to the practical achievement of the social, economic, and scientific purposes set forth in this Article; and :e. to transmit regularly to the Secretary-General for information purposes, subject to such limitation as security and constitutional considerations may require, statistical and other information of a technical nature relating to economic, social, and educational conditions in the territories for which they are respectively responsible other than those territories to which Chapters XII and XIII apply.
===Article 74===
Members of the United Nations also agree that their policy in respect of the territories to which this Chapter applies, no less than in respect of their metropolitan areas, must be based on the general principle of good-neighbourliness, due account being taken of the interests and well-being of the rest of the world, in social, economic, and commercial matters.
==Chapter XII - International Trusteeship System==
===Article 75===
The United Nations shall establish under its authority an international trusteeship system for the administration and supervision of such territories as may be placed thereunder by subsequent individual agreements. These territories are hereinafter referred to as trust territories.
===Article 76===
The basic objectives of the trusteeship system, in accordance with the Purposes of the United Nations laid down in Article 1 of the present Charter, shall be: :a. to further international peace and security; :b. to promote the political, economic, social, and educational advancement of the inhabitants of the trust territories, and their progressive development towards self-government or independence as may be appropriate to the particular circumstances of each territory and its peoples and the freely expressed wishes of the peoples concerned, and as may be provided by the terms of each trusteeship agreement; :c. to encourage respect for human rights and for fundamental freedoms for all without distinction as to race, sex, language, or religion, and to encourage recognition of the interdependence of the peoples of the world; and :d. to ensure equal treatment in social, economic, and commercial matters for all Members of the United Nations and their nationals, and also equal treatment for the latter in the administration of justice, without prejudice to the attainment of the foregoing objectives and subject to the provisions of Article 80.
===Article 77===
# The trusteeship system shall apply to such territories in the following categories as may be placed thereunder by means of trusteeship agreements: :a. territories now held under mandate; :b. territories which may be detached from enemy states as a result of the Second World War; and :c. territories voluntarily placed under the system by states responsible for their administration.
# It will be a matter for subsequent agreement as to which territories in the foregoing categories will be brought under the trusteeship system and upon what terms.
===Article 78===
The trusteeship system shall not apply to territories which have become Members of the United Nations, relationship among which shall be based on respect for the principle of sovereign equality.
===Article 79===
The terms of trusteeship for each territory to be placed under the trusteeship system, including any alteration or amendment, shall be agreed upon by the states directly concerned, including the mandatory power in the case of territories held under mandate by a Member of the United Nations, and shall be approved as provided for in Articles 83 and 85.
===Article 80===
# Except as may be agreed upon in individual trusteeship agreements, made under Articles 77, 79, and 81, placing each territory under the trusteeship system, and until such agreements have been concluded, nothing in this Chapter shall be construed in or of itself to alter in any manner the rights whatsoever of any states or any peoples or the terms of existing international instruments to which Members of the United Nations may respectively be parties.
# Paragraph 1 of this Article shall not be interpreted as giving grounds for delay or postponement of the negotiation and conclusion of agreements for placing mandated and other territories under the trusteeship system as provided for in Article 77.
===Article 81===
The trusteeship agreement shall in each case include the terms under which the trust territory will be administered and designate the authority which will exercise the administration of the trust territory. Such authority, hereinafter called the administering authority, may be one or more states or the Organization itself.
===Article 82===
There may be designated, in any trusteeship agreement, a strategic area or areas which may include part or all of the trust territory to which the agreement applies, without prejudice to any special agreement or agreements made under Article 43.
===Article 83===
# All functions of the United Nations relating to strategic areas, including the approval of the terms of the trusteeship agreements and of their alteration or amendment shall be exercised by the Security Council.
# The basic objectives set forth in Article 76 shall be applicable to the people of each strategic area.
# The Security Council shall, subject to the provisions of the trusteeship agreements and without prejudice to security considerations, avail itself of the assistance of the Trusteeship Council to perform those functions of the United Nations under the trusteeship system relating to political, economic, social, and educational matters in the strategic areas.
===Article 84===
It shall be the duty of the administering authority to ensure that the trust territory shall play its part in the maintenance of international peace and security. To this end the administering authority may make use of volunteer forces, facilities, and assistance from the trust territory in carrying out the obligations towards the Security Council undertaken in this regard by the administering authority, as well as for local defence and the maintenance of law and order within the trust territory.
===Article 85===
# The functions of the United Nations with regard to trusteeship agreements for all areas not designated as strategic, including the approval of the terms of the trusteeship agreements and of their alteration or amendment, shall be exercised by the General Assembly.
# The Trusteeship Council, operating under the authority of the General Assembly shall assist the General Assembly in carrying out these functions.
==Chapter XIII - The Trusteeship Council==
===Composition===
====Article 86====
# The Trusteeship Council shall consist of the following Members of the United Nations: :a. those Members administering trust territories; :b. such of those Members mentioned by name in Article 23 as are not administering trust territories; and :c. as many other Members elected for three-year terms by the General Assembly as may be necessary to ensure that the total number of members of the Trusteeship Council is equally divided between those Members of the United Nations which administer trust territories and those which do not.
# Each member of the Trusteeship Council shall designate one specially qualified person to represent it therein.
===Functions and Powers===
====Article 87====
The General Assembly and, under its authority, the Trusteeship Council, in carrying out their functions, may: a. consider reports submitted by the administering authority; b. accept petitions and examine them in consultation with the administering authority; c. provide for periodic visits to the respective trust territories at times agreed upon with the administering authority; and d. take these and other actions in conformity with the terms of the trusteeship agreements.
====Article 88====
The Trusteeship Council shall formulate a questionnaire on the political, economic, social, and educational advancement of the inhabitants of each trust territory, and the administering authority for each trust territory within the competence of the General Assembly shall make an annual report to the General Assembly upon the basis of such questionnaire.
===Voting===
====Article 89====
# Each member of the Trusteeship Council shall have one vote.
# Decisions of the Trusteeship Council shall be made by a majority of the members present and voting.
===Procedure===
====Article 90====
# The Trusteeship Council shall adopt its own rules of procedure, including the method of selecting its President.
# The Trusteeship Council shall meet as required in accordance with its rules, which shall include provision for the convening of meetings on the request of a majority of its members.
====Article 91====
The Trusteeship Council shall, when appropriate, avail itself of the assistance of the Economic and Social Council and of the specialized agencies in regard to matters with which they are respectively concerned.
==Chapter XIV - The International Court of Justice==
===Article 92===
The [[w:International Court of Justice|International Court of Justice]] shall be the principal judicial organ of the United Nations. It shall function in accordance with the annexed Statute, which is based upon the Statute of the Permanent Court of International Justice and forms an integral part of the present Charter.
===Article 93===
# All Members of the United Nations are ipso facto parties to the Statute of the International Court of Justice.
# A state which is not a Member of the United Nations may become a party to the Statute of the International Court of Justice on conditions to be determined in each case by the General Assembly upon the recommendation of the Security Council.
===Article 94===
# Each Member of the United Nations undertakes to comply with the decision of the International Court of Justice in any case to which it is a party.
# If any party to a case fails to perform the obligations incumbent upon it under a judgment rendered by the Court, the other party may have recourse to the Security Council, which may, if it deems necessary, make recommendations or decide upon measures to be taken to give effect to the judgment.
===Article 95===
Nothing in the present Charter shall prevent Members of the United Nations from entrusting the solution of their differences to other tribunals by virtue of agreements already in existence or which may be concluded in the future.
===Article 96===
# The General Assembly or the Security Council may request the International Court of Justice to give an advisory opinion on any legal question.
# Other organs of the United Nations and specialized agencies, which may at any time be so authorized by the General Assembly, may also request advisory opinions of the Court on legal questions arising within the scope of their activities.
==Chapter XV - The Secretariat==
===Article 97===
The Secretariat shall comprise a Secretary-General and such staff as the Organization may require. The Secretary-General shall be appointed by the General Assembly upon the recommendation of the Security Council. He shall be the chief administrative officer of the Organization.
===Article 98===
The Secretary-General shall act in that capacity in all meetings of the General Assembly, of the Security Council, of the Economic and Social Council, and of the Trusteeship Council, and shall perform such other functions as are entrusted to him by these organs. The Secretary-General shall make an annual report to the General Assembly on the work of the Organization.
===Article 99===
The Secretary-General may bring to the attention of the Security Council any matter which in his opinion may threaten the maintenance of international peace and security.
===Article 100===
# In the performance of their duties the Secretary-General and the staff shall not seek or receive instructions from any government or from any other authority external to the Organization. They shall refrain from any action which might reflect on their position as international officials responsible only to the Organization.
# Each Member of the United Nations undertakes to respect the exclusively international character of the responsibilities of the Secretary-General and the staff and not to seek to influence them in the discharge of their responsibilities.
===Article 101===
# The staff shall be appointed by the Secretary-General under regulations established by the General Assembly.
# Appropriate staffs shall be permanently assigned to the Economic and Social Council, the Trusteeship Council, and, as required, to other organs of the United Nations. These staffs shall form a part of the Secretariat.
# The paramount consideration in the employment of the staff and in the determination of the conditions of service shall be the necessity of securing the highest standards of efficiency, competence, and integrity. Due regard shall be paid to the importance of recruiting the staff on as wide a geographical basis as possible.
==Chapter XVI - Miscellaneous Provisions==
===Article 102===
# Every treaty and every international agreement entered into by any Member of the United Nations after the present Charter comes into force shall as soon as possible be registered with the Secretariat and published by it.
# No party to any such treaty or international agreement which has not been registered in accordance with the provisions of paragraph 1 of this Article may invoke that treaty or agreement before any organ of the United Nations.

===Article 103===
In the event of a conflict between the obligations of the Members of the United Nations under the present Charter and their obligations under any other international agreement, their obligations under the present Charter shall prevail.
===Article 104===
The Organization shall enjoy in the territory of each of its Members such legal capacity as may be necessary for the exercise of its functions and the fulfilment of its purposes.
===Article 105===
# The Organization shall enjoy in the territory of each of its Members such privileges and immunities as are necessary for the fulfilment of its purposes.
# Representatives of the Members of the United Nations and officials of the Organization shall similarly enjoy such privileges and immunities as are necessary for the independent exercise of their functions in connexion with the Organization.
# The General Assembly may make recommendations with a view to determining the details of the application of paragraphs 1 and 2 of this Article or may propose conventions to the Members of the United Nations for this purpose.
==Chapter XVII - Transitional Security Arrangements==
===Article 106===
Pending the coming into force of such special agreements referred to in Article 43 as in the opinion of the Security Council enable it to begin the exercise of its responsibilities under Article 42, the parties to the Four-Nation Declaration, signed at Moscow, 30 October 1943, and France, shall, in accordance with the provisions of paragraph 5 of that Declaration, consult with one another and as occasion requires with other Members of the United Nations with a view to such joint action on behalf of the Organization as may be necessary for the purpose of maintaining international peace and security.
===Article 107===
Nothing in the present Charter shall invalidate or preclude action, in relation to any state which during the Second World War has been an enemy of any signatory to the present Charter, taken or authorized as a result of that war by the Governments having responsibility for such action.
==Chapter XVIII - Amendments==
===Article 108===
Amendments to the present Charter shall come into force for all Members of the United Nations when they have been adopted by a vote of two thirds of the members of the General Assembly and ratified in accordance with their respective constitutional processes by two thirds of the Members of the United Nations, including all the permanent members of the Security Council.
===Article 109===
# A General Conference of the Members of the United Nations for the purpose of reviewing the present Charter may be held at a date and place to be fixed by a two-thirds vote of the members of the General Assembly and by a vote of any nine members of the Security Council.
Each Member of the United Nations shall have one vote in the conference.
# Any alteration of the present Charter recommended by a two-thirds vote of the conference shall take effect when ratified in accordance with their respective constitutional processes by two thirds of the Members of the United Nations including all the permanent members of the Security Council.
# If such a conference has not been held before the tenth annual session of the General Assembly following the coming into force of the present Charter, the proposal to call such a conference shall be placed on the agenda of that session of the General Assembly, and the conference shall be held if so decided by a majority vote of the members of the General Assembly and by a vote of any seven members of the Security Council.
==Chapter XIX - Ratification and Signature==
===Article 110===
# The present Charter shall be ratified by the signatory states in accordance with their respective constitutional processes.
# The ratifications shall be deposited with the Government of the United States of America, which shall notify all the signatory states of each deposit as well as the Secretary-General of the Organization when he has been appointed.
# The present Charter shall come into force upon the deposit of ratifications by the Republic of China, France, the Union of Soviet Socialist Republics, the United Kingdom of Great Britain and Northern Ireland, and the United States of America, and by a majority of the other signatory states. A protocol of the ratifications deposited shall thereupon be drawn up by the Government of the United States of America which shall communicate copies thereof to all the signatory states.
# The states signatory to the present Charter which ratify it after it has come into force will become original Members of the United Nations on the date of the deposit of their respective ratifications.
===Article 111===
The present Charter, of which the Chinese, French, Russian, English, and Spanish texts are equally authentic, shall remain deposited in the archives of the Government of the United States of America. Duly certified copies thereof shall be transmitted by that Government to the Governments of the other signatory states.
IN FAITH WHEREOF the representatives of the Governments of the United Nations have signed the present Charter.
DONE at the city of San Francisco the twenty-sixth day of June, one thousand nine hundred and forty-five
"""

    else:
        raise ValueError("unknown document")

def split_document(doctext):
    """in: text of a document
    out: set of document tokens with whitespace removed"""
    return string.split(doctext, None)

GRADING = 5

def setup_logging(filename="output.log", grading=False):
    global GRADING
    logging.addLevelName(GRADING, "GRADING")
    logger = logging.getLogger()
    logger.setLevel(0)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    chformatter = logging.Formatter("[%(levelname)s] %(message)s")
    ch.setFormatter(chformatter)
    logger.addHandler(ch)
    if grading:
        fh = logging.FileHandler(filename)
        fhformatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(fhformatter)
        logger.addHandler(fh)
