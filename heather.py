import org.heather.api.enums as enums
import org.heather.discoverer as discoverer

a = discoverer.FileDiscoverer(directories=[
    {'path': '../', 'recursive': True},
    {'path': '.', 'recursive': False}
])
print(len(a.discover()))