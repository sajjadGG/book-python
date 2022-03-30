class Config:
    title: Optional[str] = None
    anystr_lower: bool = False
    anystr_strip_whitespace: bool = False
    min_anystr_length: int = 0
    max_anystr_length: Optional[int] = None
    validate_all: bool = False
    extra: Extra = Extra.ignore
    allow_mutation: bool = True
    frozen: bool = False
    allow_population_by_field_name: bool = False
    use_enum_values: bool = False
    fields: Dict[str, Union[str, Dict[str, str]]] = {}
    validate_assignment: bool = False
    error_msg_templates: Dict[str, str] = {}
    arbitrary_types_allowed: bool = False
    orm_mode: bool = False
    getter_dict: Type[GetterDict] = GetterDict
    alias_generator: Optional[Callable[[str], str]] = None
    keep_untouched: Tuple[type, ...] = ()
    schema_extra: Union[Dict[str, Any], 'SchemaExtraCallable'] = {}
    json_loads: Callable[[str], Any] = json.loads
    json_dumps: Callable[..., str] = json.dumps
    # key type should include ForwardRef, but that breaks with python3.6
    json_encoders: Dict[Union[Type[Any], str], AnyCallable] = {}
    underscore_attrs_are_private: bool = False

    # whether inherited models as fields should be reconstructed as base model
    copy_on_model_validation: bool = True
    # whether `Union` should check all allowed types before even trying to coerce
    smart_union: bool = False
