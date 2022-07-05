class Groups:
    def get_ids(power_bi_client: PowerBiClient):
        groups_service = power_bi_client.groups()
        groups = groups_service.get_groups()

        ids = []

        for group in groups["value"]:
            group_id = group["id"]

            paramsgroup = {
                'id': 'e191fc4b-db78-4320-bf25-993cbf339640',
                'isReadOnly': False,
                'isOnDedicatedCapacity': False,
                'type': 'Workspace',
                'name': 'Rental Manutenção'
            }
            sql = """
            INSERT into powerbi.refreshes(id, isReadOnly, isOnDedicatedCapacity, type, name)
            VALUES (%(id)s, %(isReadOnly)s, %(isOnDedicatedCapacity)s, %(type)s, %(name)s)
            """
            engine_from_config.execute(sql, paramsgroup)



