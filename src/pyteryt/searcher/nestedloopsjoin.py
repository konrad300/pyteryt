class NestedLoopsJoin(object):
    def join(self, outer, inner, condition):
        result = []
        for outer_item in outer:
            for inner_item in inner:
                if condition(outer_item, inner_item):
                    merged = self.__merge_objects(outer_item, inner_item)
                    result.append(merged)
        return result

    def __merge_objects(self, object1, object2):
        merged = dict()
        merged.update(object1)
        merged.update(object2)
        return merged
