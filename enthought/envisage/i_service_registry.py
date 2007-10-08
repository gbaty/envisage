""" The service registry interface. """


# Enthought library imports.
from enthought.traits.api import Interface


class IServiceRegistry(Interface):
    """ The service registry interface.

    The service registry provides a 'Yellow Pages' style mechanism, in that
    services are published and looked up by protocol (meaning, *interface*,
    *type*, or *class* (for old-style classes!). It is called a 'Yellow Pages'
    mechanism because it is just like looking up a telephone number in the
    'Yellow Pages' phone book. You use the 'Yellow Pages' instead of the
    'White Pages' when you don't know the *name* of the person you want to
    call but you do know what *kind* of service you require. For example, if
    you have a leaking pipe, you know you need a plumber, so you pick up your
    'Yellow Pages', go to the 'Plumbers' section and choose one that seems to
    fit the bill based on price, location, certification, etc. The service
    registry does exactly the same thing as the 'Yellow Pages', only with
    objects, and it even allows you to publish your own entries for free
    (unlike the *real* one)!
    
    """

    def get_service(self, protocol, query='', minimize='', maximize=''):
        """ Return at most one service that matches the specified query.

        Return None if no such service is found.

        If no query is specified then a service that provides the specified
        protocol is returned (if one exists).
        
        NOTE: If more than one service exists that match the criteria then
        Don't try to guess *which* one it will return - it is random!

        """

    def get_services(self, protocol, query='', minimize='', maximize=''):
        """ Return all services that match the specified query.

        If no services match the query, then an empty list is returned.

        If no query is specified then all services that provide the specified
        protocol are returned (if any exist).

        """
        
    def get_service_properties(self, service_id):
        """ Return the dictionary of properties associated with a service.

        If no such service exists a 'ValueError' exception is raised.

        The properties returned are 'live' i.e. changing them immediately
        changes the service registration.
        
        """

    def register_service(self, protocol, obj, properties=None):
        """ Register a service.

        Returns a service Id that can be used to retrieve any service
        properties, and to unregister the service.
        
        """
        
    def unregister_service(self, service_id):
        """ Unregister a service.

        If no such service exists a 'ValueError' exception is raised.

        """

#### EOF ######################################################################
