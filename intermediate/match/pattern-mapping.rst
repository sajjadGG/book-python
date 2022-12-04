Match Pattern Mapping
=====================

A *mapping pattern* looks like ``{"user": u, "emails": [*es]}``. It
matches mappings with at least the set of provided keys, and if all the
sub-patterns match their corresponding values. It binds whatever the
sub-patterns bind while matching with the values corresponding to the
keys. Adding **rest at the end of the pattern to capture extra items
is allowed.
