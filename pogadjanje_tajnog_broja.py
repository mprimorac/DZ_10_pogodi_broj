'''Igra pogađanja brojeva za Python 3.x. Program je nadogradnja prethodno napisanog programa iste namjene, 
koji je sada napisan korištenjem funkcija.'''

def generiranje_tajnog_broja():
	'''Funkcija generira tajni broj i vraća ga dalje...'''
	from random import randint, seed #Poziv funkcija iz modula random.
	seed() #Postavljanje početnog stanja generatora pseudo-slučajnih brojeva na slučajno :-)
	tajni_broj = randint(0, 9) #Generiranje broja i upisivanje u varijablu.
	return tajni_broj #Izlazna vrijednost iz funkcije.

def main():
	'''Glavna funkcija. Ispisuje pozdravnu poruku, upute o igri, traži unos broja, usporedjuje i ispisuje rezultat.'''
	print('Program je igra pogađanja brojeva!\nGeneriran je tajni broj od 0-9, koji trebate pogoditi!')
	pokušaj = int(input('Upišite neki broj od 0-9: ')) #Unos broja od strane korisnika.
	broj_pokušaja = 1 #Postavljanje varijable broja pokušaja na jedan.
	tajni_broj = generiranje_tajnog_broja() #Pozivanje funkcije i upisivanje njezine izlazne vrijednosti u varijablu
	while pokušaj != tajni_broj: #Petlja za provjeru rezultata.
		pokušaj = int(input('Niste pogodili, pokušajte ponovo: ')) #Unos novog broja.
		broj_pokušaja += 1 #Inkrementiranje broja pokušaja za jedan.
	print('Pogodili ste broj u {}. pokušaju! Traženi broj je bio broj {}!'.format(broj_pokušaja, tajni_broj))

if __name__ == '__main__':
	main()
