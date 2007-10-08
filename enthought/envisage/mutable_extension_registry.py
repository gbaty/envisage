""" A mutable, manually populated extension registry. """


# Enthought library imports.
from enthought.traits.api import implements

# Local imports.
from extension_registry import ExtensionRegistry
from i_mutable_extension_registry import IMutableExtensionRegistry
from unknown_extension import UnknownExtension


class MutableExtensionRegistry(ExtensionRegistry):
    """ A mutable, manually populated extension registry. """

    implements(IMutableExtensionRegistry)
    
    ###########################################################################
    # 'IMutableExtensionRegistry' interface.
    ###########################################################################

    def add_extension(self, extension_point_id, extension):
        """ Contribute an extension to an extension point. """

        self.add_extensions(extension_point_id, [extension])

        return

    def add_extensions(self, extension_point_id, extensions):
        """ Contribute a list of extensions to an extension point. """

        self._lk.acquire()
        try:
            self._check_extension_point(extension_point_id)
            
            old   = self._get_extensions(extension_point_id)
            index = len(old)
            old.extend(extensions)

            refs = self._get_listener_refs(extension_point_id)

        finally:
            self._lk.release()
            
        # Let any listeners know that the extensions have been added.
        self._call_listeners(refs, extension_point_id, extensions, [], index)
        
        return
    
    def remove_extension(self, extension_point_id, extension):
        """ Remove a contribution from an extension point. """

        self.remove_extensions(extension_point_id, [extension])
        
        return

    def remove_extensions(self, extension_point_id, extensions):
        """ Remove a list of contributions from an extension point. """

        self._lk.acquire()
        try:
            for extension in extensions:
                try:
                    self._get_extensions(extension_point_id).remove(extension)

                except ValueError:
                    raise UnknownExtension(extension_point_id, extension)

            refs = self._get_listener_refs(extension_point_id)

        finally:
            self._lk.release()

        # Let any listeners know that the extensions have been removed.
        self._call_listeners(refs, extension_point_id, [], extensions, None)

        return

    def set_extensions(self, extension_point_id, extensions):
        """ Set the extensions to an extension point. """

        self._lk.acquire()
        try:
            old = self._get_extensions(extension_point_id)
            self._extensions[extension_point_id] = extensions

            refs = self._get_listener_refs(extension_point_id)

        finally:
            self._lk.release()

        # Let any listeners know that the extensions have been set.
        self._call_listeners(refs, extension_point_id, extensions, old, None)

        return

#### EOF ######################################################################
