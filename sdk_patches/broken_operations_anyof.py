import sys


# apparently, this patch applies to all operations-fields as the codegen
# recognizes the schema for identical schemas to be the same and
# therefore only generating a single one (there is no separate
# SigPropOperationsInner etc being generated)
def broken_operations_anyof(sdk):
    """
    PREPARATION MODULE SDK - broken `anyOf` for all operations-types
    arrays in requestBody of POST-'/prepare' endpoint

    sdk-patch required to mitigate problems with deserialization of
    operations array: there is no `actual_instance`
    generated when calling `PrepareRequestPreparationOperationsInner`.
    """

    print(
        "\033[0;31mRUNNING PREPARATION MODULE-SDK-PATCH 'broken_operations_anyof'\033[0m",
        file=sys.stderr,
    )

    unpatched___init__ = sdk.models.BagInfoOperationsInner.__init__

    def new_init(self, *args, **kwargs):
        if "type" in kwargs or "args" in kwargs:
            if kwargs["type"] == "complement":
                instance = sdk.models.ComplementOperation(**kwargs)
            elif kwargs["type"] == "overwriteExisting":
                instance = sdk.models.OverwriteExistingOperation(**kwargs)
            elif kwargs["type"] == "findAndReplace":
                instance = sdk.models.FindAndReplaceOperation(**kwargs)
            elif kwargs["type"] == "findAndReplaceLiteral":
                instance = sdk.models.FindAndReplaceLiteralOperation(**kwargs)
            else:
                raise ValueError(
                    f"""Unknown operation type '{kwargs["type"]}'."""
                )
        else:
            raise sdk.exceptions.BadRequestException(
                status=400,
                reason=(
                    "Element in '.preparation.<X>Operations' missing "
                    + "required property 'type'."
                )
            )
        unpatched___init__(self, actual_instance=instance, *args, **kwargs)

    sdk.models.BagInfoOperationsInner.__init__ = new_init
