"use client"

import { useForm } from 'react-hook-form'

type Props = {}

const Form = (props: Props) => {

    const { register, handleSubmit } = useForm()

  return (
    <section>
        <form onSubmit={handleSubmit(data=>console.log(data))}>
            <input type="text" placeholder='text' {...register('name')}/>
            <button type='submit'>Submit</button>
        </form>
    </section>
  )
}

export default Form