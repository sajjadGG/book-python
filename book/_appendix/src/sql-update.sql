UPDATE kontakty SET firstname='Jose' WHERE lastname='Jimenez';

UPDATE kontakty SET
    firstname=:firstname,
    lastname=:lastname,
    adresy=:adresy
WHERE id=:id