SELECT BIO.first_name
FROM entity
INNER JOIN country on entity.countries = country.id
INNER JOIN BIO on BIO.id = entity.person
WHERE
    country.country = "USA"

